from flask import jsonify, request
from app.services.cotacao_service import CotacaoService

class CotacaoController:
    def get_cotacao(codigo):
        ativoKeys = {f'{codigo}.SA': float('0.00')}
        ativo = CotacaoService.get_cotation_yahoo(**ativoKeys).iloc[0]
        return jsonify({
            'messagem': f'Cotação do ativo {codigo}',
            'status': 'Sucesso',
            'Cotação': f'{ativo:.2f}'
        }), 200
    
    def calc_rentabilidade(ativo_id):
        print(ativo_id)
        return CotacaoService.calc_rentabilidade(ativo_id)
    
    def calc_carteira():
        return CotacaoService.calc_carteira()