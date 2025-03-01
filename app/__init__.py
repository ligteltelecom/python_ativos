from flask import Flask
from app.routes import userRoute, homeRoute
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
  
  db.init_app(app)  
  Migrate(app, db)
  
  from app.models import Usuario, Ativo
  app.register_blueprint(userRoute)
  app.register_blueprint(homeRoute)
  return app
