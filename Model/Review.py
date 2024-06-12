#!/usr/bin/python3
"""
Review module
"""

from Model.Base_Model import BaseModel


class Review(BaseModel):
    """
    Represents a review of a place by a user.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The user ID who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
