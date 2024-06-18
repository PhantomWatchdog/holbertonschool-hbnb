"""
Country module
"""

import uuid
from datetime import datetime


class Country:
    """
    Represents a country.

    Attributes:
        country_id (uuid.UUID): The unique identifier for the country.
        name (str): The name of the country.
        created_at (datetime): The date and time when the country was created.
        updated_at (datetime): The date and time when the country was last updated.
        cities (list): A list of cities in the country.
    """

    def __init__(self, name):
        self.country_id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = []
