#!/usr/bin/python3

import unittest
from datetime import datetime
from time import sleep
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

    def test_save(self):
        old_updated_at = self.amenity.updated_at
        sleep(1)
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
