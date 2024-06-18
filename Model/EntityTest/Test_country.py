import unittest
from datetime import datetime
from Model.Country import Country
import uuid


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("United States")

    def test_country_id(self):
        self.assertIsNotNone(self.country.country_id)
        self.assertIsInstance(self.country.country_id, uuid.UUID)

    def test_name(self):
        self.assertEqual(self.country.name, "United States")

    def test_created_at(self):
        self.assertIsInstance(self.country.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.country.updated_at, datetime)

    def test_cities(self):
        self.assertIsInstance(self.country.cities, list)
        self.assertEqual(len(self.country.cities), 0)

if __name__ == '__main__':
    unittest.main()