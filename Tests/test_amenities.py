#!/usr/bin/python3

import unittest
from datetime import datetime
from Class.amenities import Amenities


class TestAmenities(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenities()

    def test_init(self):
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.amenitie_id, str)
        self.assertEqual(self.amenity.name, "")
        self.assertEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
