import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.movie import Movie
from models.category import Category
from models.favorite import Favorite
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from datetime import datetime

from dotenv import load_dotenv
import os
import requests

load_dotenv()

movie_database_api_key = os.getenv("MOVIE_DATABASE_API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@localhost:3306/movie_app'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/user', methods=['POST'])
def create_user():
  data = request.json
  username = data.get('username')
  password = data.get('password')

  if username and password: 
    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user = User(username=username, password=hashed_password, role='user')
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User successfully created.'})

  return jsonify({'message': 'Invalid data'}), 400


@app.route('/login', methods=['POST'])
def login():
  data = request.json
  username = data.get('username')
  password = data.get('password')

  if username and password:
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
      login_user(user)
      print(current_user.is_authenticated)
      return jsonify({'message': 'The user signed in successfully.'})
    
  return jsonify({'message': 'Invalid credentials'}), 400

@app.route('/fetch_categories', methods=['POST'])
def fetch_categories():
  
  api_categories_url = f'https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={movie_database_api_key}'
  response_categories = requests.get(api_categories_url)
  data_categories = response_categories.json()

  if response_categories.status_code == 200:
    for category_data in data_categories.get('genres', []):
      category = Category(category_external_id=category_data['id'], title=category_data['name'])

      category_id = category_data['id']
      existing_category = Category.query.filter_by(category_external_id=category_id).first()

      if existing_category:
          continue
      
      db.session.add(category)
      db.session.commit()
    
    return jsonify({'message': 'Categories fetched and stored successfully'})
  else:
      return jsonify({'error': 'Failed to fetch categories from the API'})

@app.route('/categories', methods=['GET'])
def list_categories():
  categories = Category.query.all()
  serialized_categories = [category.serialize() for category in categories]
  return jsonify(serialized_categories)

@app.route('/fetch_movies', methods=['POST'])
def fetch_movies():
  for n in range(1, 3):  
    api_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={n}&api_key={movie_database_api_key}"
    response = requests.get(api_url)
    data = response.json()

    for movie in data['results']:
      genre_ids = movie['genre_ids']

      categories = Category.query.filter(Category.category_external_id.in_(genre_ids)).all()

      movie_categories = [category for category in categories]

      movie_data = Movie(
        title=movie['title'],
        # genre_ids=movie['genre_ids'],
        adult=movie['adult'],
        original_language=movie['original_language'],
        release_date=movie['release_date'],
        overview=movie['overview'],
        vote_average=movie['vote_average'],
        popularity=movie['popularity'],
        poster_path=movie['poster_path'],
        genres=movie_categories
      )

      existing_movie = Movie.query.filter_by(title=movie['title']).first()

      if existing_movie:
        continue

      db.session.add(movie_data)
      db.session.commit()

    return jsonify({'message': 'Movies fetched and stored successfully'})
  

      # writer.writerow([title, genre_ids, adult, original_language, release_date, overview, vote_average, popularity, poster])

@app.route('/movies', methods=['GET'])
def list_movies():
  movies = Movie.query.all()
  serialized_movies = [movie.serialize() for movie in movies]
  return jsonify(serialized_movies)

if __name__ == '__main__':
  app.run(debug=True)

