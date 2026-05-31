import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS
from config.envconfig import ENV


from middleware.error_handler import (register_error_handlers)

from routes.tokenized_data_routes import tokenize_data_bp
from routes.story_data_routes import story_data_bp

PORT = int(os.getenv("PORT", 7860))

app = Flask(__name__)
CORS(app)



BASE_URL = "/api/v1/python"


@app.route("/routes")
def routes():
    return jsonify({
        "routes": [
            {
                "path": str(rule),
                "methods": list(rule.methods)
            }
            for rule in app.url_map.iter_rules()
        ]
    })

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "SB Canada Dictionary API is running"
    })


app.register_blueprint(story_data_bp,url_prefix = BASE_URL)
app.register_blueprint(tokenize_data_bp,url_prefix=BASE_URL)




register_error_handlers(app)




if __name__ == '__main__':
       app.run(
        host="0.0.0.0",
        port=PORT,
        debug=ENV["NODE_ENV"] == "development"
    )
    