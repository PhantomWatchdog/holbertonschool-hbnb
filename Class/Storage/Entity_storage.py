#!/usr/bin/python3

import json
from Class.base_model import BaseModel
from Class.user import User
from Class.place import Place

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
                for obj_id, obj_data in objectsdict.items():
                    cls_name = obj_data.pop("__class__")
                    self.new(eval(cls_name)(**obj_data))
        except FileNotFoundError:
            return
