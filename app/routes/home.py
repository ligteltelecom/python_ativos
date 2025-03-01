from flask import Blueprint, request
from app.controllers import home_controller

homeRoute = Blueprint('home', __name__)

@homeRoute.route('/ping', methods=['GET'])
def ping():
    return home_controller.HomeController().ping()