from database import db
from datetime import datetime

movie_genre = db.Table('movie_genre',
  db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
  db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Movie(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  title = db.Column(db.String(120), nullable=False)
  adult = db.Column(db.Boolean, nullable=False, default=False)
  original_language = db.Column(db.String(4), nullable=False, default="en")
  overview = db.Column(db.String(5000), nullable=False)
  vote_average = db.Column(db.Float, nullable=False)
  popularity = db.Column(db.Integer, nullable=False)
  poster_path = db.Column(db.String(180), nullable=False)
  release_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

  category = db.relationship('Category', backref='movies')
  
  # Define a different backref title for the genres relationship
  genres = db.relationship('Category', secondary=movie_genre, backref=db.backref('associated_movies', lazy='dynamic'))

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'adult': self.adult,
      'original_language': self.original_language,
      'overview': self.overview,
      'vote_average': self.vote_average,
      'popularity': self.popularity,
      'poster_path': self.poster_path,
      'release_date': self.release_date.strftime('%Y-%m-%d'),
      'category': self.category.serialize() if self.category else None,
      'genres': [genre.title for genre in self.genres]  
    }