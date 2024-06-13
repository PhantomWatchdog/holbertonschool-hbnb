#!/usr/bin/python3

from Class.base_model import BaseModel


class User(BaseModel):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.mail = ""      
