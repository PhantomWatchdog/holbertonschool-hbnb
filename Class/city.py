#!/usr/bin/python3

from Class.base_model import BaseModel


class City(BaseModel):
    def __init__(self):
        self.name = ""
        self.country = ""
        self.city = ""
