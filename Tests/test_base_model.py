#!/usr/bin/python3

import unittest
from datetime import datetime
from time import sleep
from Class.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save(self):
        old_updated_at = self.model.updated_at
        sleep(1)
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):

        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at)
        self.assertEqual(model_dict['updated_at'], self.model.updated_at)
        self.assertIsInstance(model_dict, dict)

if __name__ == '__main__':
    unittest.main()