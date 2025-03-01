from datetime import datetime
from sqlalchemy.sql import func
from app.database import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.DateTime(timezone=True),default=datetime.now(),server_default=func.now())
    
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

