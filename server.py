import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS
from config.envconfig import ENV


from middleware.error_handler import (register_error_handlers)

from routes.tokenized_data_routes import tokenize_data_bp
from routes.story_data_routes import story_data_bp



app = Flask(__name__)
CORS(app)



BASE_URL = "/api/v1/python"


app.register_blueprint(story_data_bp,url_prefix = BASE_URL)
app.register_blueprint(tokenize_data_bp,url_prefix=BASE_URL)




register_error_handlers(app)




if __name__ == '__main__':
       app.run(
        host="0.0.0.0",
        port=ENV["PORT"],
        debug=ENV["NODE_ENV"] == "development"
    )
    