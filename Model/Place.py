"""
Place module
"""

import uuid
from datetime import datetime


class Place:
    """
    Represents a place object.

    Attributes:
        place_id (uuid.UUID): The unique identifier for the place.
        name (str): The name of the place.
        description (str): The description of the place.
        price (float): The price of the place.
        location (str): The location of the place.
        city_id (str): The ID of the city where the place is located.
        host_id (str): The ID of the host who owns the place.
        created_at (datetime): The date and time when the place was created.
        updated_at (datetime): The date and time when the place was last updated.
        amenities (list): The list of amenities available in the place.
        reviews (list): The list of reviews for the place.
    """

    def __init__(self, name, description, price, location, city_id, host_id):
        self.place_id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.city_id = city_id
        self.host_id = host_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []
