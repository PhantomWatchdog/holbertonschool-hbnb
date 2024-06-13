#!/usr/bin/python3
"""
Definition of the Storage class
"""

import json
from Model.Base_Model import BaseModel
from Model.User import User
from Model.Country import Country
from Model.City import City
from Model.Place import Place
from Model.Review import Review
from Model.Amenitie import Amenity

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
        return Storage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
        """
        objclsname = obj.__class__.__name__
        Storage.__objects["{}.{}".format(objclsname, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path)
        """
        serialdict = Storage.__objects
        objectsdict = {obj: serialdict[obj].to_dict() for obj in serialdict.keys()}
        with open(Storage.__file_path, "w") as jfile:
            json.dump(objectsdict, jfile)

    def reload(self):
        """
        Deserialize the JSON file (path: __file_path) to __objects
        """
        try:
            with open(Storage.__file_path, "r") as jfile:
                objectsdict = json.load(jfile)
                for oo in objectsdict.values():
                    cls_name = oo["__class__"]
                    del oo["__class__"]
                    self.new(eval(cls_name)(**oo))
        except FileNotFoundError:
            return
