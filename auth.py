# auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import usuarios

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((u for u in usuarios if u.username == username and u.password == password), None)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('welcome'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
