from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  # id (int), username (text), password(text), role (text)
  id = db.Column(db.Integer, unique=True, primary_key=True)
  username = db.Column(db.String(32), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  role = db.Column(db.String(8), nullable=False, default='user')
  favorites = db.relationship('Favorite', backref='user', lazy=True)
