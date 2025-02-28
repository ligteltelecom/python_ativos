from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from mvc_flask import FlaskMVC
from flask_migrate import Migrate
import jose
from dynaconf import Dynaconf
import datetime

db = SQLAlchemy()

class Base(DeclarativeBase):
  pass

def create_app():
  app = Flask(__name__)
  FlaskMVC(app)
  
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
    
  return app
