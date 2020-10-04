from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.hash_password(password)
    
    def hash_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
