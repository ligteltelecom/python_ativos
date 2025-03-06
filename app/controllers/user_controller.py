import datetime
import bcrypt
from app.database import db
from flask import jsonify, request
from app.modelos import Usuario
from bcrypt import hashpw, gensalt
from flask_jwt_extended import create_access_token, get_jwt_identity


class UserController:
    def login_user(request):
        try:
            user = Usuario.query.filter_by(email=request['email']).first()
            if not user:
                return jsonify({'messagem': 'Usuario não encontrado'}), 401
            if not bcrypt.checkpw(request['senha'].encode('utf-8'), user.senha):
                return jsonify({'message': 'Senha incorreta'}), 401
                        
         
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}), 409
    
    def logged():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    
    def register_user(request):
        try:
            #get the request data and insert into the table Usuario
            userRegister = Usuario(
                nome = request['nome'],
                email = request['email'],
                senha = request['senha']
            )
            
            #Ecrypt the password 
            userRegister.senha = hashpw(userRegister.senha.encode('utf-8'), gensalt())
    
            #Add the user to the database
            db.session.add(userRegister)
            db.session.commit()
            return jsonify({
                "message": "Usuario cadastrado", 
                "status": "Sucesso",
                "Usuario":{
                    "id": userRegister.id, 
                    "nome": userRegister.nome, 
                    "email": userRegister.email
                    }}),201
        
        except Exception as e:
            return jsonify({'messagem': 'Erro', 'msgErro': repr(e)}),409
        finally:
            db.session.close()
    
    def listAll():
        try:
            #Get all users from the table Usuario
            users = Usuario.query.all()            
            return jsonify({
                "messagem": "Lista de usuarios",
                "status": "Sucesso",
                "usuarios": [{
                    "id": user.id, 
                    "nome": user.nome, 
                    "email": user.email
                } for user in users]
            }),200
        except Exception as e:
            return jsonify({'message': 'Error', 'msgError': repr(e)}),409
        finally:
            db.session.close()
    
    def getUserByEmail(self, email):
        try:
            #Get the user by the email
            return Usuario.query.filter_by(email=email).one()
            
        except:
            return None 
    def checkPassword(self, userPass, requestPass):
        return bcrypt.checkpw(requestPass.encode('utf-8'), userPass.senha)
        