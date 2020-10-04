from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user
from . import login_manager, db
from .models import User
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not user.verify_password(password):
        flash('Username and or password incorrect. Please try again!')
        return render_template('login.html')
    
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

@auth_bp.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('register.html')


@auth_bp.route('/register', methods=['POST'])
def register_post():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('User email already exists.')
        return redirect(url_for('auth.register'))
    
    new_user = User(email=email, name=name, password=password)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
    

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
