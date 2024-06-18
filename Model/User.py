"""
Definition of the User class
"""
import uuid
from datetime import datetime


class User:
    """
    Represents a user in the system.

    Attributes:
        user_id (str): The unique identifier for the user.
        email (str): The email address of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        password (str): The password of the user.
        created_at (datetime): The date and time when the user was created.
        updated_at (datetime): The date and time when the user was last updated.
        places (list): A list of places associated with the user.
    """

    def __init__(self, email, first_name, last_name, password):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
