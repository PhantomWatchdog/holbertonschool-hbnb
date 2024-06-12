#!/usr/bin/python3
"""
City module
"""

from Model.Base_Model import BaseModel


class City(BaseModel):
    """City class.

    Attributes:
        country_id (str): The ID of the country.
        name (str): The name of the city.
    """
    country_id = ""
    name = ""
