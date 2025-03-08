from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from app.controllers.ativo_controller import AtivoController
from app.controllers.cotacao_controller import CotacaoController

ativoRoute = Blueprint('ativos', __name__)

@ativoRoute.route('/ativos', methods=['GET'])
@jwt_required()
def listAll():
   return AtivoController().getAtivos()

@ativoRoute.route('/ativos', methods=['POST'])
@jwt_required()
def register_ativo(): 
    return AtivoController.register_ativo(request.get_json())

@ativoRoute.route('/ativos/<int:ativo_id>', methods=['DELETE'])
@jwt_required()
def delete_ativo(ativo_id): 
    return AtivoController.delete_ativo(ativo_id)

@ativoRoute.route('/ativos/<int:ativo_id>', methods=['PUT'])
@jwt_required()
def update_ativo(ativo_id):
    data = request.get_json() 
    return AtivoController.update_ativo(ativo_id, data)

@ativoRoute.route('/ativos/<int:ativo_id>/rentabilidade', methods=['GET'])
@jwt_required()
def calc_rentabilidade(ativo_id):
    return CotacaoController.calc_rentabilidade(ativo_id)

@ativoRoute.route('/cotacao', methods=['GET'])
def get_cotacao():
    codigo = request.get_json().get('codigo')
    return CotacaoController.get_cotacao(codigo)