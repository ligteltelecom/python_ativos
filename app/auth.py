import datetime
from flask import jsonify, request, current_app
import jwt
from app.controllers import user_controller

def authetication():
    auth = request.get_json()    
    msgError = {'messagem': 'Unauthorized', 'status': 'Erro'}
    
    senha = auth.get('senha', None) 
    email = auth.get('email', None)
    
    if not auth or not email or not senha:
        return jsonify({'messagem': 'Usuario ou senha incorretos', 'status': 'Erro'}), 401
    
    user = user_controller.UserController().getUserByEmail(email)
    if not user:
        return jsonify({'messagem': 'Usuario nao encontrado', 'status': 'Erro'}), 401
    
    userPass = user_controller.UserController().checkPassword(user, senha)
        
    if user and  userPass:
        token = jwt.encode({
            'user_id': user.id, 
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)
            }, 
            current_app.config['SECRET_KEY'],
            algorithm='HS256')        
        return jsonify({'token': token, 'status': 'Sucesso'}), 200
 
    
    return jsonify(msgError), 401
   
    