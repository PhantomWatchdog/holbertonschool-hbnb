from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class City(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.String(36), db.ForeignKey('countries.country_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    places = db.relationship('Place', backref='city', lazy=True)

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id