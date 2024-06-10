#!/usr/bin/python3
"""
Definition of the Storage class
"""

import json
from datetime import datetime
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
        try:
            with open(self.__file_path, "r", encoding="utf-8") as jsonfile:
                json_dict = json.load(jsonfile)
                for key, value in json_dict.items():
                    value['created_at'] = datetime.strptime(value['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    value['updated_at'] = datetime.strptime(value['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_class = eval(key.split(".")[0])
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
