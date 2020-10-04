from flask import Blueprint, render_template
from flask_login import login_required, current_user


route_bp = Blueprint('main', __name__)

@route_bp.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@route_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)