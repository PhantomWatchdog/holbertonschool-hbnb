#!/usr/bin/python3

import unittest
from datetime import datetime
from Class.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country()

    def test_init(self):
        self.assertIsInstance(self.country.id, str)
        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)
        self.assertEqual(self.country.name, "")
        self.assertEqual(self.country.created_at, self.country.updated_at)

if __name__ == '__main__':
    unittest.main()