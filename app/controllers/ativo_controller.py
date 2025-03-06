from flask import jsonify
from app.database import db
from app.modelos import Ativo

class AtivoController:
    def getAtivos(self):
        try:
            ativos = Ativo.query.all()
            
            return jsonify({
                "messagem": "Lista de Ativos",
                "status": "Sucesso",
                "ativos": [{
                    "id": ativo.id,
                    "codigo": ativo.codigo,
                    "nome": ativo.nome,                
                    "tipo": ativo.tipo,
                    "preco": ativo.preco,
                    "data_aquisicao": ativo.data_aquisicao,            
                } for ativo in ativos]
            }), 200
            
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}),409

        
    def register_ativo(data):
        try:
            ativo = Ativo(
                user_id=data['user_id'],
                codigo=data['codigo'],
                nome=data['nome'],
                tipo=data['tipo'],
                preco=data['preco']
            )
            
            db.session.add(ativo)
            db.session.commit()
            
            return jsonify({
                "messagem": "Ativo cadastrado",
                "status": "Sucesso",
                "Ativo": {
                    "id": ativo.id,
                    "codigo": ativo.codigo,
                    "name": ativo.nome,
                    "tipo": ativo.tipo,
                    "preco": ativo.preco,
                    "data_aquisicao": ativo.data_aquisicao
                }
            }), 201
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}),409