from app.controllers.user_controller import UserController
from app.auth import authetication
from flask import Blueprint, request

userRoute = Blueprint('users', __name__)


@userRoute.route('/auth/register', methods=['POST'])
def register_user(): 
    return UserController.register_user(request.get_json())

@userRoute.route('/users', methods=['GET'])
def listAll():
    return UserController.listAll()

@userRoute.route('/auth', methods=['POST'])
def auth():
    return authetication()