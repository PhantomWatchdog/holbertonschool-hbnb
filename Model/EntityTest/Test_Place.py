#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from datetime import datetime
from Model.Place import Place


class TestPlaceInit(unittest.TestCase):
    """test to check if attributes exists"""
    def test_has_attribute(self):
        attributes = ["id", "created_at", "updated_at", "city_id",
                    "user_id",
                    "name", "description", "number_rooms",
                    "number_bathrooms",
                    "max_guest", "price_by_night", "latitude",
                    "longitude",
                    "amenity_ids"]
        my_place = Place()
        for name in attributes:
            self.assertTrue(hasattr(my_place, name))

    def test_is_right_type(self):
        my_place = Place()
        self.assertIsInstance(my_place.id, str)
        self.assertIsInstance(my_place.created_at, datetime)
        self.assertIsInstance(my_place.updated_at, datetime)
        self.assertIsInstance(my_place.city_id, str)
        self.assertIsInstance(my_place.name, str)
        self.assertIsInstance(my_place.description, str)
        self.assertIsInstance(my_place.number_rooms, int)
        self.assertIsInstance(my_place.number_bathrooms, int)
        self.assertIsInstance(my_place.max_guest, int)
        self.assertIsInstance(my_place.price_by_night, int)
        self.assertIsInstance(my_place.latitude, float)
        self.assertIsInstance(my_place.longitude, float)
        self.assertIsInstance(my_place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()