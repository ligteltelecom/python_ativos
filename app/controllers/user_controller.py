import bcrypt
from app.database import db
from flask import jsonify, request
from app.modelos import Usuario
from bcrypt import hashpw, gensalt

class UserController:
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
    
    def getUserByEmail(self, email):
        try:
            #Get the user by the email
            return Usuario.query.filter_by(email=email).one()
            
        except:
            return None 
    def checkPassword(self, userPass, requestPass):
        return bcrypt.checkpw(requestPass.encode('utf-8'), userPass.senha)
        