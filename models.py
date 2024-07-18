# models.py

class Usuario:
    def __init__(self, id, username, password, es_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin

# Creando tres usuarios de prueba
usuarios = [
    Usuario(1, 'user1', 'password1'),
    Usuario(2, 'user2', 'password2'),
    Usuario(3, 'admin', 'adminpassword', es_admin=True)
]
