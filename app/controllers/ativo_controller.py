from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.database import db
from app.modelos import Ativo

class AtivoController:
    
    def getAtivos(self):
        try:            
            current_user_id = get_jwt_identity()
            ativos = Ativo.query.filter_by(user_id = current_user_id).all()
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
            current_user_id = get_jwt_identity()
            ativo = Ativo(
                user_id = current_user_id,
                codigo = data['codigo'],
                nome = data['nome'],
                tipo = data['tipo'],
                preco = data['preco']
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
        finally:
            db.session.close()
        
    def update_ativo(ativo_id,data):
        try:
            current_user_id = get_jwt_identity()
                    
            ativo = Ativo.query.filter_by(id = ativo_id, user_id = current_user_id).first()
            
            if not ativo:
                return jsonify({'messagem': 'Ativo não encontrado', 'status': 'Erro'}), 404
            
            
            ativo.codigo = data['codigo']
            ativo.nome = data['nome']
            ativo.tipo = data['tipo']
            ativo.preco = data['preco']
            
            db.session.commit()
            
            
            return jsonify({
                "messagem": "Ativo atualizado",
                "status": "Sucesso",
                "Ativo": {
                    "id": ativo.id,
                    "codigo": ativo.codigo,
                    "name": ativo.nome,
                    "tipo": ativo.tipo,
                    "preco": ativo.preco,
                    "data_aquisicao": ativo.data_aquisicao
                }
            }), 200
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}),409
        finally:
            db.session.close()
        
    def delete_ativo(id):
        try:
            current_user_id = get_jwt_identity()
            ativo = Ativo.query.filter_by(id = id, user_id = current_user_id).first()
            
            if not ativo:
                return jsonify({'messagem': 'Ativo não encontrado', 'status': 'Erro'}), 404
            
            db.session.delete(ativo)
            db.session.commit()
            
            return jsonify({'messagem': 'Ativo deletado', 'status': 'Sucesso'}), 200
            
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}),409
        finally:
            db.session.close()

                