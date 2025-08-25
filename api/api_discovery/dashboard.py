from asyncio import Task
from datetime import datetime
from tracemalloc import start
from database.models import LaneDefinition, ProcessDefinition, TaskInstance
from flask import app, request, jsonify, session
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


    @app.route('/getNCRCDashboard', methods=['GET'])
    def get_ncrc_dashboard():
        """
        Retrieves the NCRC dashboard data
        Returns JSON data only - use: (Invoke-WebRequest -Uri 'http://localhost:5656/getNCRCDashboard' -Method GET).Content | ConvertFrom-Json

        $response = Invoke-WebRequest -Uri 'http://localhost:5656/getNCRCDashboard' -Method GET
        $jsonString = [System.Text.Encoding]::UTF8.GetString($response.Content)
        $jsonString | ConvertFrom-Json
        """
        app_logger.info('Retrieving NCRC dashboard data')
        # Implement your logic to retrieve and return the NCRC dashboard data:
        from database.models import WFApplication, LaneDefinition, TaskInstance
        app_obj = WFApplication.query.first()
        stage_obj = LaneDefinition.query.filter_by(LaneName='Initial').first()
        task_objs = TaskInstance.query.all()
        
        # Build the structured response
        result = {
            "applications": app_obj.to_dict() if app_obj else {},
            "stages": {},
            "tasks": [task.to_dict() for task in task_objs] if task_objs else []
        }
        
        # Organize tasks by stage/lane
        if stage_obj:
            stage_name = stage_obj.to_dict()["LaneName"]
            result["stages"][stage_name] = {
                "stage_info": stage_obj.to_dict(),
                "tasks": [task.to_dict() for task in task_objs] if task_objs else []
            }
        
        app_logger.info(f'NCRC dashboard data retrieved successfully: {result}')
        return jsonify({"status": "ok", "data": result}), 200