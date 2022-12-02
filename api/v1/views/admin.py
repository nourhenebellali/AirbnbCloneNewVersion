#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask_jwt_extended import create_access_token


@app_views.route('/admin/login', methods=['GET'], strict_slashes=False)
def login():
    """
    Login to the admin panel
    """
    token = create_access_token(identity='admin')
    return jsonify({"token": token}), 200


@app_views.route('/admin/signup', methods=['GET'], strict_slashes=False)
def signup():
    """
    Signup to the admin panel
    """
    token = create_access_token(identity='admin')
    return jsonify({"token": token}), 200

