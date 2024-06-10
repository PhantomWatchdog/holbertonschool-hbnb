#!/usr/bin/python3
"""
Definition of the Storage class
"""

import json
import os
from Model.Base_Model import Model
from Model.user import User

class Storage:
    """
    Storage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path)
        """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """
        Deserialize the JSON file (path: __file_path) to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                dict = json.load(file)
            for key, value in dict.items():
                cls = Model.__dict__[value["__class__"]]
                obj = cls(**value)
                self.__objects[key] = obj
