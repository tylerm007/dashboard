from multiprocessing import process
import datetime, os
from decimal import Decimal
from logic_bank.exec_row_logic.logic_row import LogicRow
from logic_bank.extensions.rule_extensions import RuleExtension
from logic_bank.logic_bank import Rule
from logic_bank.logic_bank import DeclareRule
import database.models as models
import api.system.opt_locking.opt_locking as opt_locking
from security.system.authorization import Grant, Security
from logic.load_verify_rules import load_verify_rules
import integration.kafka.kafka_producer as kafka_producer
import logging
from config import Config

app_logger = logging.getLogger(__name__)

declare_logic_message = "ALERT:  *** No Rules Yet ***"  # printed in api_logic_server.py

def declare_logic():
    ''' Declarative multi-table derivations and constraints, extensible with Python.
 
    Brief background: see readme_declare_logic.md
    
    Your Code Goes Here - Use code completion (Rule.) to declare rules
    '''

    if os.environ.get("WG_PROJECT"):
        # Inside WG: Load rules from docs/expprt/export.json
        load_verify_rules()
    else:
        # Outside WG: load declare_logic function
        from logic.logic_discovery.auto_discovery import discover_logic
        discover_logic()

    def handle_all(logic_row: LogicRow):  # #als: TIME / DATE STAMPING, OPTIMISTIC LOCKING
        """
        This is generic - executed for all classes.

        Invokes optimistic locking, and checks Grant permissions.

        Also provides user/date stamping.

        Args:
            logic_row (LogicRow): from LogicBank - old/new row, state
        """

        if os.getenv("APILOGICPROJECT_NO_FLASK") is not None:
            print("\ndeclare_logic.py Using TestBase\n")
            return  # enables rules to be used outside of Flask, e.g., test data loading

        if logic_row.is_updated() and logic_row.old_row is not None and logic_row.nest_level == 0:
            opt_locking.opt_lock_patch(logic_row=logic_row)

        Grant.process_updates(logic_row=logic_row)
        did_stamping = False
        enable_stamping = True
        if enable_stamping:  # #als:  DATE / USER STAMPING
            row = logic_row.row
            if logic_row.ins_upd_dlt == "ins" and hasattr(row, "CreatedDate"):
                row.CreatedDate = datetime.datetime.now()
                did_stamping = True
            if logic_row.ins_upd_dlt == "ins" and hasattr(row, "CreatedBy"):
                row.CreatedBy = Security.current_user().id
                #    if Config.SECURITY_ENABLED == True else 'public'
                did_stamping = True
            if logic_row.ins_upd_dlt == "upd" and hasattr(row, "ModifiedDate"):
                row.ModifiedDate = datetime.datetime.now()
                did_stamping = True
            if logic_row.ins_upd_dlt == "upd" and hasattr(row, "ModifiedBy"):
                row.ModifiedBy = Security.current_user().id  \
                    if Config.SECURITY_ENABLED == True else 'public'
                did_stamping = True
            if did_stamping:
                logic_row.log("early_row_event_all_classes - handle_all did stamping")     
    Rule.early_row_event_all_classes(early_row_event_all_classes=handle_all)

    #als rules report
    from api.system import api_utils
    # api_utils.rules_report()

    def test_state_change(row: models.TaskInstance, old_row: models.TaskInstance, logic_row:LogicRow):
        '''
        Only validate state change (update) if the status is changing using TaskFlow
        PEND -> NEW
        NEW -> INP
        INP -> COMP
        '''
        if logic_row.ins_upd_dlt == 'upd' and row.Status != old_row.Status:
            pass

            next_tasks = row.ToTaskTaskFlowList
            for task in next_tasks:
                if task.ToTaskId == row.TaskId and task.Condition in (None, '', '1=1', 'True'):
                    return
            pass
        return True
    
    #Rule.constraint(validate=models.TaskInstance,calling=test_state_change,error_msg="TaskInstance Status can only change forward")
    '''
    def start_workflow(logic_row: LogicRow):
        """
        Start the workflow for a New Application 
        """
        if logic_row.ins_upd_dlt != 'ins':
            return
        from api.api_discovery.workflow import _start_workflow as start_workflow_function
        process_name = "Application Workflow"
        application_id = logic_row.row.ApplicationId
        started_by = logic_row.row.StartedBy
        priority = logic_row.row.Priority
        start_workflow_function(process_name=process_name, application_id=application_id, started_by=started_by, priority=priority)
        
        
    Rule.after_flush_row_event(on_class=models.WFApplication, calling=start_workflow)

    

    #WF Application Dashboard
    Rule.count(derive=models.WFDashboard.count_completed,as_count_of=models.WFApplication, where=lambda row: row.status == 'COMP')
    Rule.count(derive=models.WFDashboard.count_in_progress,as_count_of=models.WFApplication, where=lambda row: row.status == 'INP')
    Rule.count(derive=models.WFDashboard.count_new,as_count_of=models.WFApplication, where=lambda row: row.status == 'NEW') 
    Rule.count(derive=models.WFDashboard.count_withdrawn,as_count_of=models.WFApplication, where=lambda row: row.status == 'WTH')
    Rule.count(derive=models.WFDashboard.total_count,as_count_of=models.WFApplication)
 

    Rule.count(derive=models.StageInstance.TotalCount, as_count_of=models.TaskInstance)
    Rule.count(derive=models.StageInstance.CompletedCount, as_count_of=models.TaskInstance, where=lambda row: row.Status == 'COMP')
    '''
    app_logger.debug("..logic/declare_logic.py (logic == rules + code)")

