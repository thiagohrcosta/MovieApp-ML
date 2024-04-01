from database import db
from datetime import datetime

class Category(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  title = db.Column(db.String(32), nullable=False)
  movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

