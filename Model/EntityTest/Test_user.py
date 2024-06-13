#!/usr/bin/python3
"""
unittest sequences for user.py.

Sequences:
    TestUser_instantiation
"""

import Model
import unittest
from datetime import datetime
from Model.User import User
from time import sleep


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """
        Test case to verify that User class can be instantiated
        without any arguments.
        """
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """
        Test if a new instance of User is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(User(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the id attribute
        of the User class is of type str.

        It creates a new instance of the User class
        and checks if the type of its id attribute is str.
        """
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """
        Test that the `created_at` attribute
        of the User class is of type datetime.
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test that the `updated_at` attribute
        of the User class is of type datetime.
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """
        Test case to verify that the email attribute
        of User class is of type str.
        """
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """
        Test case to verify that the password attribute
        of User class is of type str.
        """
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """
        Test case to check if the `first_name` attribute
        of the User class is of type str.
        """
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """
        Test that the `last_name` attribute
        of the User class is of type str.
        """
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """
        Test case to verify that two User instances have unique ids.
        """
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_two_users_different_created_at(self):
        """
        Test case to verify that two users
        have different 'created_at' timestamps.
        """
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_two_users_different_updated_at(self):
        """
        Test that two User instances have different updated_at values.
        """
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of the User object.

        This method verifies that the __str__ method
        of the User class returns the expected string representation.
        It checks if the string contains the user's ID, 'id' key-value pair,
        'created_at' key-value pair, and 'updated_at' key-value pair.
        """
        date = datetime.today()
        date_repr = repr(date)
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = date
        usrstr = usr.__str__()
        self.assertIn("[User] (123456)", usrstr)
        self.assertIn("'id': '123456'", usrstr)
        self.assertIn("'created_at': " + date_repr, usrstr)
        self.assertIn("'updated_at': " + date_repr, usrstr)

    def test_args_unused(self):
        """
        Test case to verify that the User object
        does not contain any unused arguments.

        This test creates a User object with None as the argument
        and checks that None is not present
        in the values of the User object's dictionary (__dict__).
        """
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test case to verify the instantiation of User
        object with keyword arguments.

        This test case checks if the User object is instantiated
        correctly when provided with keyword arguments.
        It verifies if the attributes of the instantiated object
        match the provided values.

        Steps:
        1. Get the current date and time.
        2. Convert the date and time to ISO format.
        3. Instantiate a User object with the provided keyword arguments.
        4. Assert that the id attribute of the User object
        matches the provided value.
        5. Assert that the created_at attribute of the User object
        matches the current date and time.
        6. Assert that the updated_at attribute of the User object
        matches the current date and time.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        usr = User(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(usr.id, "345")
        self.assertEqual(usr.created_at, date)
        self.assertEqual(usr.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that User instantiation raises
        a TypeError when passed None as arguments.
        This is because these arguments are expected to be non-None values.
        """
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)
