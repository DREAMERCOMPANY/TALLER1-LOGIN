# app.py

from flask import Flask, session, redirect, url_for, render_template
from auth import auth
from models import usuarios

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.register_blueprint(auth)

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
            perros = ["Perro 1", "Perro 2", "Perro 3"]
            return render_template('admin.html', user=user, perros=perros)
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
