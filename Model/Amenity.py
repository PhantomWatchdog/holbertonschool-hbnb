#!/usr/bin/python3
"""
Amenity module
"""

import uuid
from datetime import datetime


class Amenity:
    """
    Represents an amenity.

    Attributes:
        amenity_id (uuid.UUID): The unique identifier for the amenity.
        name (str): The name of the amenity.
        created_at (datetime.datetime): The date and time when the amenity was created.
        updated_at (datetime.datetime): The date and time when the amenity was last updated.
    """

    def __init__(self, name):
        self.amenity_id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
