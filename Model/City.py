"""
City module
"""

import uuid
from datetime import datetime


class City:
    """
    Represents a city.

    Attributes:
        city_id (uuid.UUID): The unique identifier for the city.
        name (str): The name of the city.
        country_id (str): The identifier of the country the city belongs to.
        created_at (datetime): The date and time when the city was created.
        updated_at (datetime): The date and time when the city was last updated.
        places (list): A list of places associated with the city.
    """

    def __init__(self, name, country_id):
        self.city_id = uuid.uuid4()
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
