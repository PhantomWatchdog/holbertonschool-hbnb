import unittest
from datetime import datetime
from Model.City import City
import uuid

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("New York", "US")

    def test_city_attributes(self):
        self.assertIsInstance(self.city.city_id, uuid.UUID)
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.country_id, "US")
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.places, [])

    def test_city_id_uniqueness(self):
        another_city = City("Los Angeles", "US")
        self.assertNotEqual(self.city.city_id, another_city.city_id)

    def test_city_created_at(self):
        now = datetime.now()
        self.assertLessEqual(self.city.created_at, now)

    def test_city_updated_at(self):
        now = datetime.now()
        self.assertLessEqual(self.city.updated_at, now)

    def test_add_place(self):
        place = "Central Park"
        self.city.places.append(place)
        self.assertIn(place, self.city.places)

    def test_remove_place(self):
        place = "Central Park"
        self.city.places.append(place)
        self.city.places.remove(place)
        self.assertNotIn(place, self.city.places)

if __name__ == '__main__':
    unittest.main()