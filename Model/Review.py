"""
Review module
"""


import uuid
from datetime import datetime

class Review:
    """
    Represents a review for a place.

    Attributes:
        review_id (uuid.UUID): The unique identifier for the review.
        user_id (str): The ID of the user who made the review.
        place_id (str): The ID of the place being reviewed.
        rating (int): The rating given to the place.
        comment (str): The comment provided by the user.
        created_at (datetime.datetime): The timestamp when the review was created.
        updated_at (datetime.datetime): The timestamp when the review was last updated.
    """

    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = uuid.uuid4()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
