from flask import Blueprint
from app.controllers.home_controller import HomeController

homeRoute = Blueprint('home', __name__)

@homeRoute.route('/', methods=['GET'])
def index():
    return HomeController().index()

@homeRoute.route('/ping', methods=['GET'])
def ping():
    return HomeController().ping()