from database import db
from datetime import datetime

class Movie(db.Model):
  # id (int), name (text), description (text), date (Date), time (time), is_in_diet (boolean), user_id (ForeignKey)
  id = db.Column(db.Integer, unique=True, primary_key=True)
  title = db.Column(db.String(32), nullable=False)
  overview = db.Column(db.String(500), nullable=False)
  vote_average = db.Column(db.Float(4), nullable=False)
  popularity = db.Column(db.Integer, nullable=False)
  poster_path = db.Column(db.String(80), nullable=False)
  release_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  categories = db.relationship('Category', backref='user', lazy=True)


