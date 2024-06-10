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
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    now = datetime.now()
                    time = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            Model.Storage.new(self)

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
        obj_dict = self.__dict__.copy()
        obj_dict.update({"__class__": self.__class__.__name__,
                        "created_at": self.created_at.isoformat(),
                        "updated_at": self.updated_at.isoformat()})

        return obj_dict

    def __str__(self):
        """
        Return a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"