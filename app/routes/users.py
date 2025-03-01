from flask import Blueprint, request
from app.controllers import user_controller
from app.auth import authetication


userRoute = Blueprint('users', __name__)

@userRoute.route('/auth/register', methods=['POST'])
def register_user(): 
    user = user_controller.UserController()
    return user.register_user(request.get_json())

@userRoute.route('/users', methods=['GET'])
def listAll():
    user = user_controller.UserController()
    return user.listAll()

@userRoute.route('/auth', methods=['POST'])
def auth():
    return authetication()