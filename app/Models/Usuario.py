from datetime import datetime
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    nome = db.Column(db.String(100), nullable=False),
    email = db.Column(db.String(100), unique=True, nullable=False),
    senha = db.Column(db.String(100), nullable=False),
    data_criacao = db.Column(db.DateTime, default=datetime.datetime.now)


