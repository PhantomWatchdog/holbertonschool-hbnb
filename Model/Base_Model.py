#!/usr/bin/python3
"""
Definition of the BaseModel class
"""

import Model
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    BaseModel class

    Attributes:
        id (str): The unique identifier of the object.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        time_format = ("%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            Model.Storage.new(self)

    def save(self):
        """
        Save the object
        """
        self.updated_at = datetime.today()
        Model.Storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the object

        Returns:
            dict: A dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the object

        Returns:
            str: A string representation of the object.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
