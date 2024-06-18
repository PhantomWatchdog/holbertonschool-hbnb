import unittest
from datetime import datetime
from Model.Place import Place
import uuid


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place("Cozy Apartment", "A cozy apartment in the city center", 100.0, "City Center", "12345", "67890")

    def test_attributes(self):
        self.assertIsInstance(self.place.place_id, uuid.UUID)
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.description, "A cozy apartment in the city center")
        self.assertEqual(self.place.price, 100.0)
        self.assertEqual(self.place.location, "City Center")
        self.assertEqual(self.place.city_id, "12345")
        self.assertEqual(self.place.host_id, "67890")
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertEqual(self.place.amenities, [])
        self.assertEqual(self.place.reviews, [])

    def test_update_attributes(self):
        self.place.name = "Luxury Villa"
        self.place.description = "A luxurious villa with a private pool"
        self.place.price = 500.0
        self.place.location = "Beachfront"
        self.place.city_id = "54321"
        self.place.host_id = "09876"
        self.place.updated_at = datetime.now()

        self.assertEqual(self.place.name, "Luxury Villa")
        self.assertEqual(self.place.description, "A luxurious villa with a private pool")
        self.assertEqual(self.place.price, 500.0)
        self.assertEqual(self.place.location, "Beachfront")
        self.assertEqual(self.place.city_id, "54321")
        self.assertEqual(self.place.host_id, "09876")
        self.assertIsInstance(self.place.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()