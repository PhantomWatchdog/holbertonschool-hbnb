#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from datetime import datetime
from Model.user import User


class TestUserInit(unittest.TestCase):
    """test to check if attributes exists"""
    def test_has_attribute(self):
        attributes = ["id", "created_at", "updated_at", "email", "password",
                    "first_name", "last_name"]
        my_user = User()
        for name in attributes:
            self.assertTrue(hasattr(my_user, name))

    def test_is_right_type(self):
        my_user = User()
        self.assertIsInstance(my_user.id, str)
        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)
        self.assertIsInstance(my_user.email, str)
        self.assertIsInstance(my_user.password, str)
        self.assertIsInstance(my_user.first_name, str)
        self.assertIsInstance(my_user.last_name, str)


if __name__ == '__main__':
    unittest.main()