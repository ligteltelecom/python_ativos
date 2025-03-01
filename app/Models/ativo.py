from datetime import datetime
from sqlalchemy.sql import func
from app.database import db

class Ativo(db.Model):
    __tablename__ = 'ativos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(10), nullable=False) 
    tipo = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric, nullable=False)
    data_aquisicao = db.Column(db.DateTime(timezone=True),default=datetime.now(),server_default=func.now())