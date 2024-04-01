from database import db
from datetime import datetime

class Favorite(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)