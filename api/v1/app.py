#!/usr/bin/python3
""" Flask Application """
from models import storage
from datetime import timedelta

from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'holbieQuickreport'

app.config['JWT_SECRET_KEY'] = 'Qucikreportadmin'
@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


JWTManager(app)

def create_app():
    app = Flask(__name__)
    # app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_blueprint(app_views)
    app.config['SECRET_KEY'] = 'admin'
    app.config['JWT_SECRET_KEY'] = 'admin'
    
    ACCESS_EXPIRES = timedelta(hours=24)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES #Token Time Auto Revoke
    app.config['JWT_BLACKLIST_ENABLED'] = True # Enable Token Blocklist
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh'] #Type of Token
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    JWTManager(app)
    storage.reload()


    return app