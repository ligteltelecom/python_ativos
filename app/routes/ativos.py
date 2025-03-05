from flask import Blueprint, Response, request
from app.controllers.ativo_controller import AtivoController

ativoRoute = Blueprint('ativos', __name__)

@ativoRoute.route('/ativos', methods=['GET'])
def listAll():
   return AtivoController().getAtivos()