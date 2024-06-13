#!/usr/bin/python3

from Class.base_model import BaseModel


class Place(BaseModel):
    def __init__(self):
        self.place_id = ""
        self.name = ""
        self.description = ""
        self.nb_rooms = 0
        self.nb_bathrooms = 0
        self.city_id = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.max_guests = 0
        self.price_per_night = 0
        self.amenitie = []
        self.user_id = ""
