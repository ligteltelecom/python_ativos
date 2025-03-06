from flask_jwt_extended import jwt_required
from app.controllers.user_controller import UserController
from app.auth import authetication
from flask import Blueprint, request

userRoute = Blueprint('users', __name__)

@userRoute.route('/auth/login', methods=['POST'])
def login_user():
    return UserController.login_user(request.get_json())

@userRoute.route('/auth', methods=['GET'])
@jwt_required()
def logged():
    return UserController.logged()

@userRoute.route('/auth/register', methods=['POST'])
def register_user(): 
    return UserController.register_user(request.get_json())

@userRoute.route('/users', methods=['GET'])
@jwt_required()
def listAll():
    return UserController.listAll()

@userRoute.route('/auth/loginoff', methods=['POST'])
def auth():
    return authetication()