from flask import jsonify
from app.models import Ativo

class AtivoController:
    def getAtivos(self):
        ativos = Ativo.query.all()
        return jsonify({
            "message": "List of Ativos",
            "status": "Success",
            "Ativos": [{
                "id": ativo.id,
                "codigo": ativo.codigo,
                "name": ativo.name,                
                "tipo": ativo.tipo,
                "preco": ativo.preco,
                "data_aquisicao": ativo.data_aquisicao,            
            } for ativo in ativos]
        }), 200