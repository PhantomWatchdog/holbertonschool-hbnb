#!/usr/bin/python3
"""
Definition of the BaseModel class
"""

import Model
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.__dict__.update(kwargs)

    def save(self):
        """
        Save the object
        """
        self.updated_at = datetime.now()
        Model.Storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the object
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        """
        Return a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    