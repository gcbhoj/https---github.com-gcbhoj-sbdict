import json
import os
from flasgger import Swagger
from flask import Flask,jsonify,request
from flask_cors import CORS
from config.envconfig import ENV


from middleware.error_handler import (register_error_handlers)
from config.swagger_config import SWAGGER_CONFIG,SWAGGER_TEMPLATE

from routes.tokenized_data_routes import tokenize_data_bp
from routes.story_data_routes import story_data_bp

PORT = int(os.getenv("PORT", 7860))

app = Flask(__name__)
CORS(app)

Swagger(app, config=SWAGGER_CONFIG, template=SWAGGER_TEMPLATE)

BASE_URL = "/api/v1/python"


@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "SB Canada Dictionary API is running"
    })
    
@app.route("/debug/files")
def debug_files():
    import os

    return {
            "app_exists": os.path.exists("/app"),
            "data_exists": os.path.exists("/app/data"),
            "files": os.listdir("/app"),
            "data_files": os.listdir("/app/data") if os.path.exists("/app/data") else []
        }


app.register_blueprint(story_data_bp,url_prefix = BASE_URL)
app.register_blueprint(tokenize_data_bp,url_prefix=BASE_URL)




register_error_handlers(app)




if __name__ == '__main__':
       app.run(
        host="0.0.0.0",
        port=PORT,
        debug=ENV["NODE_ENV"] == "development"
    )
    