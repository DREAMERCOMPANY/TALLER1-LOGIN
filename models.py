# models.py
from db import db

#Crear clases
class Usuario:
    def __init__(self, id, username, password, es_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin

class Guarderias(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(45), nullable = False)
    Dirección = db.Column(db.String(45), nullable = False)
    Telefono = db.Column(db.String(45), nullable = False)

class Perros(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Raza = db.Column(db.String(45), nullable=False)
    Edad = db.Column(db.Integer, nullable=False)
    Peso = db.Column(db.Float, nullable=False)


# Creando los tres usuarios
usuarios = [
    Usuario(1, 'superman@correo.co', 'superman123'),
    Usuario(2, 'marvel@marver.co', 'marvel123'),
    Usuario(3, 'admin@correo.co', 'adminpassword', es_admin=True)
]



