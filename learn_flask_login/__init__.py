import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config_factory

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

from .auth import auth_bp
from .routes import route_bp
from .models import User

def create_app():
    app = Flask(__name__)
    config_object = config_factory.get(os.environ.get('FLASK_ENV') or 'default')
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(auth_bp)
    app.register_blueprint(route_bp)


    return app
