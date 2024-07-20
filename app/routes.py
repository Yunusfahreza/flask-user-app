from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('main.users'))
        flash('Invalid username or password')
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.home'))

@main.route('/users')
def users():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    users = User.query.all()
    return render_template('users.html', users=users)