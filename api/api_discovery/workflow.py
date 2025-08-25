from asyncio import Task
from datetime import datetime
from tracemalloc import start
from database.models import ProcessDefinition, TaskInstance
from flask import request, jsonify, session
import logging
import pyodbc
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

    @app.route('/hello_service')
    def hello_service():
        """        
        Illustrates:
        * Use standard Flask, here for non-database endpoints.

        Test it with PowerShell POST:
        
        $body = @{
            user = "ApiLogicServer"
        } | ConvertTo-Json
        
        Invoke-RestMethod -Uri "http://localhost:5656/hello_service" -Method POST -Body $body -ContentType "application/json"
        """
        user = request.args.get('user')
        app_logger.info(f'{user}')
        return jsonify({"result": f'hello from new_service! from {user}'})

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

        from database.models import ProcessDefinition, TaskDefinition, ProcessInstance, WorkflowHistory
        # Get ProcessId
        row = ProcessDefinition.query.filter_by(ProcessName=process_name, IsActive=True).first()
        if not row:
                raise Exception(f'Process definition not found: {process_name}')
        process_id = str(row.ProcessId)

        print(f'ProcessDefinition ProcessId: {process_id}')

        # Get StartTaskId
        row = TaskDefinition.query.filter_by(ProcessId=process_id, TaskType='Event', TaskCategory='Start').order_by(TaskDefinition.Sequence).first()
        start_task_id = str(row.TaskId) if row else None

        # Create new InstanceId
        instance_id = str(uuid.uuid4())
        process_instance = ProcessInstance(
            InstanceId=instance_id,
            ProcessId=process_id,
            ApplicationId=int(application_id),
            CurrentTaskId=start_task_id,
            StartedBy=started_by,
            Priority=priority
        )
        session.add(process_instance)
        session.commit()
        process_instance_id = str(process_instance.InstanceId)
        # Insert into ProcessInstances
        print(f'New ProcessInstance InstanceId: {process_instance_id}')
        # Log History
        history_instance_id = str(uuid.uuid4())
        wf_history = WorkflowHistory(
                HistoryId=history_instance_id,
                InstanceId=process_instance_id,
                TaskInstanceId=start_task_id,
                Action='Workflow Started',
                NewStatus='ACTIVE',
                ActionBy=started_by,
                ActionReason=f'New application id: {application_id} submitted for processing'
        )
        #session.add(wf_history)
        #session.commit()
        print(f'New InstanceId: {instance_id}')
        # TODO - use TaskFlow to only create starting tasks?
        rows = TaskDefinition.query.filter_by(ProcessId=process_id).all()
        for row in rows:
            print(f'TaskDefinition: {row.TaskName}')
            instance_id = str(uuid.uuid4())
            task_instance = TaskInstance(
                TaskInstanceId=instance_id,
                InstanceId=process_instance_id,
                TaskId=str(row.TaskId),
                LaneId=str(row.LaneId),
                Status='PEND',
                CreatedDate=datetime.utcnow(),
                CreatedBy=started_by
            )
            session.add(task_instance)
            session.commit()
        return instance_id