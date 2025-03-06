from io import StringIO
from flask import current_app
import requests

class CotacaoService:
    def get_cotacao(codigo):
        APIKEY =  current_app.config['SECRET_KEY']
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={codigo}.SAO&apikey={APIKEY}'
        return  requests.get(url).json()