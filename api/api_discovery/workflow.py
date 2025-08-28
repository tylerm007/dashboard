from asyncio import Task
from datetime import datetime
from database.models import ProcessDefinition, TaskDefinition, ProcessInstance, WorkflowHistory, StageInstance, TaskInstance, LaneDefinition
from flask import request, jsonify, session
import logging
import uuid
import safrs

app_logger = logging.getLogger("api_logic_server_app")
db = safrs.DB 
session = db.session 
_project_dir = None

def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators = []):
    global _project_dir
    _project_dir = project_dir
    pass

    @app.route('/start_workflow', methods=['POST','OPTIONS'])
    def start_workflow():
        """
        Illustrates:
        * Use standard Flask, here for non-database endpoints.

        Test it with PowerShell POST:

        $body = @{
                process_name = "Application Workflow"
                application_id = "1"
                started_by = "1"
                priority = "HIGH"
        } | ConvertTo-Json

        Invoke-RestMethod -Uri "http://localhost:5656/start_workflow" -Method POST -Body $body -ContentType "application/json"
        """

        # Extract variables from request.args
        process_name = request.args.get('process_name',"Application Workflow")
        application_id = request.args.get('application_id', '1')
        started_by = request.args.get('started_by','admin')
        priority = request.args.get('priority', 'Normal')  # Default to 'Normal' if not provided

        return _start_workflow(process_name, int(application_id), started_by, priority)

    def _start_workflow(process_name:str, application_id:int, started_by:str, priority:str):

        # Get ProcessId
        row = ProcessDefinition.query.filter_by(ProcessName=process_name, IsActive=True).first()
        if not row:
                raise Exception(f'Process definition not found: {process_name}') 
        process_id = row.ProcessId

        print(f'ProcessDefinition ProcessId: {process_id}')

        # Get StartTaskId
        row = TaskDefinition.query.filter_by(ProcessId=process_id, TaskType='Event', TaskCategory='Start').order_by(TaskDefinition.Sequence).first()
        start_task_id = row.TaskId if row else None

        if not start_task_id:
                raise Exception(f'Start Task definition not found for process: {process_name}')
        print(f'Start TaskDefinition TaskId: {start_task_id}')  
        # Create new Process InstanceId for this Application
        #instance_id = str(uuid.uuid4())
        process_instance = ProcessInstance(
            #InstanceId=instance_id,
            ProcessId=process_id,
            ApplicationId=int(application_id),
            CurrentTaskId=start_task_id,
            StartedBy=started_by,
            Priority=priority
        )
        session.add(process_instance)
        session.commit()
        process_instance_id = process_instance.InstanceId
        # Insert into ProcessInstances
        print(f'New ProcessInstance InstanceId: {process_instance_id}')
        # Log History
        #history_instance_id = str(uuid.uuid4())
       
     
        # TODO - use TaskFlow to only create starting tasks?
        lanes = LaneDefinition.query.filter_by(ProcessId=process_id).all()
        for lane in lanes:
                print(f'LaneDefinition: {lane.LaneName}')
                #stage_instance_id = str(uuid.uuid4())
                lane_instance = StageInstance(
                    #StageInstanceId=stage_instance_id,
                    ProcessInstanceId=process_instance_id,
                    LaneId=lane.LaneId,
                    Status='NEW',
                    CreatedDate=datetime.utcnow(),
                    CreatedBy=started_by
                )
                session.add(lane_instance)
                session.commit()
               
                rows = TaskDefinition.query.filter_by(ProcessId=process_id).all() # LaneId=lane.LaneId
                for row in rows:
                        print(f'TaskDefinition: {row.TaskName}')
                        #instance_id = str(uuid.uuid4())
                        task_instance = TaskInstance(
                                #TaskInstanceId=instance_id,
                                InstanceId=process_instance_id,
                                TaskId=row.TaskId,
                                #LaneId=row.LaneId,
                                StageId=StageInstance.StageInstanceId,
                                Status='PEND',
                                CreatedDate=datetime.utcnow(),
                                CreatedBy=started_by
                        )
                        session.add(task_instance)
                        session.commit()
                        print(f'New TaskInstance: {row.TaskName}')
                        wf_history = WorkflowHistory(
                                #HistoryId=history_instance_id,
                                InstanceId=process_instance_id,
                                TaskInstanceId=task_instance.TaskInstanceId,
                                Action=row.TaskName,
                                NewStatus='ACTIVE',
                                ActionBy=started_by,
                                ActionReason=f'New application id: {application_id} Task added to workflow'
                        )
                        session.add(wf_history)
                        session.commit()

        return jsonify({"status": "ok", "data": {"process_instance_id": process_instance_id}}), 200     