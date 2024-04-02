from database import db
from datetime import datetime

class Category(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  category_external_id = db.Column(db.Integer, unique=True)
  title = db.Column(db.String(32), nullable=False)

  def serialize(self):

    return {
      'id': self.id,
      'category_external_id': self.category_external_id,
      'title': self.title,
    }