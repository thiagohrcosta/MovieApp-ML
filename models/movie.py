from database import db
from datetime import datetime

class Movie(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  title = db.Column(db.String(32), nullable=False)
  overview = db.Column(db.String(500), nullable=False)
  vote_average = db.Column(db.Float, nullable=False)
  popularity = db.Column(db.Integer, nullable=False)
  poster_path = db.Column(db.String(80), nullable=False)
  release_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

  category = db.relationship('Category', backref='movies')

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'overview': self.overview,
      'vote_average': self.vote_average,
      'popularity': self.popularity,
      'poster_path': self.poster_path,
      'release_date': self.release_date.strftime('%Y-%m-%d'),
      'category': self.category.serialize() if self.category else None
    }