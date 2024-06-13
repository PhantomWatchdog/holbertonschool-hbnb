#!/usr/bin/python3

from Class.base_model import BaseModel


class Review(BaseModel):
    def __init__(self):
        self.review_id = ""
        self.place_id = ""
        self.content = ""
