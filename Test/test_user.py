#!/usr/bin/python3

import unittest
from datetime import datetime
from Class.user import User


class TestUserInit(unittest.TestCase):
    def test_has_attribute(self):
        attributes = ["first_name", "last_name", "mail", "password",
                      "id", "created_at", "updated_at"]
        user = User()
        for name in attributes:
            self.assertTrue(hasattr(user, name))

    def test_is_right_type(self):
        user = User()
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.mail, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_save_method(self):
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['first_name'], user.first_name)
        self.assertEqual(user_dict['last_name'], user.last_name)
        self.assertEqual(user_dict['mail'], user.mail)
        self.assertEqual(user_dict['password'], user.password)
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()