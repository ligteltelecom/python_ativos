from io import StringIO
from flask import current_app, jsonify
import requests

from app.modelos.ativo import Ativo

class CotacaoService:
    def get_cotacao(codigo):
        try:
            APIKEY =  current_app.config['SECRET_KEY']
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={codigo}.SAO&apikey={APIKEY}'
            return  requests.get(url).json()
        except Exception as e:
            return jsonify({'messagem': 'Erro ao buscar cotação','status': 'Erro', 'msgErro': repr(e)}), 500
    
    def calc_rentabilidade(ativo_id):
        try:
            ativo = Ativo.query.filter_by(id=ativo_id).first()
            
            if not ativo:
                return jsonify({'messagem': 'Ativo não encontrado', 'status': 'Erro'}), 404
            
            ativo_preco_atual = CotacaoService.get_cotacao(ativo.codigo)['Global Quote']['05. price']
            rentabilidade = ((float(ativo_preco_atual) / float(ativo.preco)) -1) * 100
            return jsonify({'rentabilidade': f'{rentabilidade}%'})
        
        except Exception as e:
            return jsonify({'messagem': 'Erro ao calcular rentabilidade','status': 'Erro','msgErro': repr(e)}), 500
            