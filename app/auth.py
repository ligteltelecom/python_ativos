import datetime
from flask import jsonify, request, current_app
import jwt
from app.controllers import user_controller

def authetication():
    auth = request.get_json()    
    msgError = {'message': 'Unauthorized', 'status': 'Error'}
    
    if not auth or not auth["email"] or not auth["senha"]:
        return jsonify({'message': 'The username or password you entered is incorrect', 'status': 'Error'}), 401
    
    user = user_controller.UserController().getUserByEmail(auth["email"])
    if not user:
        return jsonify({'message': 'User not found', 'status': 'Error'}), 401
    
    userPass = user_controller.UserController().checkPassword(user, auth["senha"])
        
    if user and  userPass:
        token = jwt.encode({
            'public_id': user.id, 
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)
            }, 
            current_app.config['SECRET_KEY'],
            algorithm='HS256')        
        return jsonify({'token': token, 'status': 'Sucess'}), 200
 
    
    return jsonify(msgError), 401
   
    