#!/usr/bin/python3

import unittest
from datetime import datetime
from Class.place import Place


class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.place_id, str)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.nb_rooms, 0)
        self.assertEqual(place.nb_bathrooms, 0)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.max_guests, 0)
        self.assertEqual(place.price_per_night, 0)
        self.assertEqual(place.amenitie, [])
        self.assertEqual(place.user_id, "")

if __name__ == "__main__":
    unittest.main()
