#!/usr/bin/python3
"""
Definition of the User class
"""

from Model.Base_Model import BaseModel


class User(BaseModel):
    """
    User class represents a user in the system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
