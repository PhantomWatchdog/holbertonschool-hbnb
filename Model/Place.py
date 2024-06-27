from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Place(db.Model):
    """
    Represents a place for rent.
    """
    place_id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('city.city_id'), nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('host.host_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    # Assuming 'Amenity' and 'Review' are other models related to 'Place'
    amenities = db.relationship('Amenity', backref='place', lazy=True)
    reviews = db.relationship('Review', backref='place', lazy=True)

    def __init__(self, name, description, price, location, city_id, host_id):
        self.place_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.city_id = city_id
        self.host_id = host_id