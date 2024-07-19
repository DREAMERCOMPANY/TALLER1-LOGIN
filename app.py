# app.py

from models import *
from db import *
from flask import Flask, session, redirect, url_for, render_template
from auth import auth
from models import usuarios

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.secret_key = 'supersecretkey'
app.register_blueprint(auth)
db.init_app(app)


@app.route('/')
def home():
    return redirect(url_for('auth.login'))

@app.route('/welcome')
def welcome():
    user_id = session.get('user_id')
    if user_id:
        user = next((u for u in usuarios if u.id == user_id), None)
        if user:
            if user.es_admin:
                return redirect(url_for('admin'))
            return render_template('welcome.html', user=user)
    return redirect(url_for('auth.login'))

@app.route('/admin')
def admin():
    user_id = session.get('user_id')
    if user_id:
        user = next((u for u in usuarios if u.id == user_id), None)
        if user and user.es_admin:
            # Simulamos una lista de perros
            #perros = ["Perro 1", "Perro 2", "Perro 3"]
            nombres_perros = Perros.query.with_entities(Perros.Nombre).all()
            perros = [nombre.Nombre for nombre in nombres_perros]
            return render_template('admin.html', user=user, perros=perros)
            #return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
