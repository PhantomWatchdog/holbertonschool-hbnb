#!/usr/bin/python3
"""
Definition of the User class
"""

from Model.Base_Model import BaseModel

class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""