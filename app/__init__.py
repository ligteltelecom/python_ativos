from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from app.routes import userRoute, homeRoute, ativoRoute
from app.database import db

from flask_migrate import Migrate
from dynaconf import Dynaconf

def create_app():
  app = Flask(__name__)
  
  settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
  )
   
  app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.MODIFICATIONS
  app.config['SECRET_KEY'] = settings.SECRET_KEY
  app.config['API_KEY'] = settings.API_KEY
  app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
  app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
  app.config['JWT_VERIFY_SUB']=False
  
  jwt = JWTManager(app)
  db.init_app(app)  
  Migrate(app, db)
  
  from app.modelos import Usuario, Ativo
  app.register_blueprint(userRoute)
  app.register_blueprint(homeRoute)
  app.register_blueprint(ativoRoute)
  return app
