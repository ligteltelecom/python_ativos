import bcrypt
from app import db
from flask import jsonify, request
from app.models import Usuario
from bcrypt import hashpw, gensalt

class UserController:
    def register_user(self):
        try:
            request_data = request.get_json()
          
            userRegister = Usuario(
               request_data['nome'],
               request_data['email'],      
               request_data['senha']           
            )
            
            #Ecrypt the password 
            userRegister.senha = bcrypt.hashpw(userRegister.senha.encode('utf-8'), bcrypt.gensalt())
    
            #Add the user to the database
            db.session.add(userRegister)
            db.session.commit()
            return jsonify({'message': 'User registered'}),201
        
        except Exception as e:
            return jsonify({'message': 'Error', 'msgError': repr(e)}),500