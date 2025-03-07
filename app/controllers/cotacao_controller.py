from flask import request
from app.services.cotacao_service import CotacaoService

class CotacaoController:
    def get_cotacao(codigo):
        return CotacaoService.get_cotacao(codigo)
    
    def calc_rentabilidade(ativo_id):
        print(ativo_id)
        return CotacaoService.calc_rentabilidade(ativo_id)