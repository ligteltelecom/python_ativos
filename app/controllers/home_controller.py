from flask import jsonify

from socket import gethostbyname, gethostname

def get_ip():
    return gethostbyname(gethostname())


class HomeController:
    def index(self):
        return jsonify({'messagem': 'Servidor esta rodando...', 'status': 'ok'}),200
    
    def ping(self):
        return jsonify({'messagem': 'Ping ok', 'ip': get_ip(),'status': 'ok'}),200