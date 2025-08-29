from flask import request, jsonify
import logging

app_logger = logging.getLogger("api_logic_server_app")

def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators = []):
    pass

    @app.route('/hello_service')
    def hello_service():
        """        
        Illustrates:
        * Use standard Flask, here for non-database endpoints.

        Test it with:
        
                http://localhost:5656/hello_service?user=ApiLogicServer
        """
        user = request.args.get('user')
        app_logger.info(f'{user}')
        return jsonify({"result": f'hello from new_service! from {user}'})
    
    @app.route('/test_api')
    def test_api():
        """
        Illustrates:
        * Use standard Flask, here for non-database endpoints.

        Test it with:

            Invoke-WebRequest -Uri "http://localhost:5656/test_api" -Method Get
        """
        from api.api_discovery.ontimize_api import getMetaData
        import requests
        tables = getMetaData(include_attributes=True)
        print(tables)
        for endpoint in tables['resources']:
            print(endpoint)
            response = requests.get(f"http://localhost:5656/api/{endpoint}?page%5Boffset%5D=0&page%5Blimit%5D=1")
            assert response.status_code == 200
            assert "data" in response.json()

            for item in response.json()["data"]:
                assert "id" in item
                assert "attributes" in item

        return jsonify({"result": "test_api completed successfully"})
