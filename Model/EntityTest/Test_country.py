#!/usr/bin/python3
"""
unittest sequences for Country.py.

Sequences:
    TestCountry_instantiation
"""

import Model
import unittest
from datetime import datetime
from time import sleep
from Model.Country import Country


class TestCountry_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Country class."""

    def test_no_args_instantiates(self):
        """
        Test case to verify that Country class
        can be instantiated without any arguments.
        """
        self.assertEqual(Country, type(Country()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of Country is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(Country(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the 'id' attribute
        of the Country class is of type str.
        """
        self.assertEqual(str, type(Country().id))

    def test_created_at_is_public_datetime(self):
        """
        Test case to verify that the `created_at` attribute
        of the Country instance is of type `datetime`.
        """
        self.assertEqual(datetime, type(Country().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the `updated_at` attribute
        of the Country class is of type datetime.
        """
        self.assertEqual(datetime, type(Country().updated_at))

    def test_name_is_public_class_attribute(self):
        """
        Test if the 'name' attribute of the Country class
        is a public class attribute.

        It checks if the 'name' attribute is of type 'str',
        if it is present in the 'dir' of an instance of the Country class,
        and if it is not present in the '__dict__' of the instance.
        """
        nation = Country()
        self.assertEqual(str, type(Country.name))
        self.assertIn("name", dir(nation))
        self.assertNotIn("name", nation.__dict__)

    def test_two_countries_unique_ids(self):
        """
        Test case to verify that two countries have unique IDs.
        """
        nation1 = Country()
        nation2 = Country()
        self.assertNotEqual(nation1.id, nation2.id)

    def test_two_countries_different_created_at(self):
        """
        Test case to verify that two countries have different
        'created_at' timestamps.
        """
        nation1 = Country()
        sleep(0.05)
        nation2 = Country()
        self.assertLess(nation1.created_at, nation2.created_at)

    def test_two_countries_different_updated_at(self):
        """
        Test that two countries have different updated_at values.
        """
        nation1 = Country()
        sleep(0.05)
        nation2 = Country()
        self.assertLess(nation1.updated_at, nation2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of the Country object.

        This test verifies that the __str__ method
        of the Country class returns the expected string representation.
        It checks that the string contains the country's ID,
        'id' attribute, 'created_at' attribute, and 'updated_at' attribute.

        Steps:
        1. Create a datetime object representing the current date and time.
        2. Get the string representation of the datetime
        object using the repr() function.
        3. Create a Country object.
        4. Set the 'id' attribute of the Country object to "123456".
        5. Set the 'created_at' and 'updated_at' attributes
        of the Country object to the datetime object.
        6. Get the string representation of the Country object
        using the __str__ method.
        7. Assert that the string contains the expected values.

        """
        date = datetime.today()
        date_repr = repr(date)
        nation = Country()
        nation.id = "123456"
        nation.created_at = nation.updated_at = date
        nationstr = nation.__str__()
        self.assertIn("[Country] (123456)", nationstr)
        self.assertIn("'id': '123456'", nationstr)
        self.assertIn("'created_at': " + date_repr, nationstr)
        self.assertIn("'updated_at': " + date_repr, nationstr)

    def test_args_unused(self):
        """
        Test that the Country object does not contain any unused arguments.
        """
        nation = Country(None)
        self.assertNotIn(None, nation.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test case to verify the instantiation of
        the Country class with keyword arguments.

        Steps:
        1. Get the current date and time using the `datetime.today()` method.
        2. Convert the date to ISO format using the `isoformat()` method.
        3. Create an instance of the Country class
        with the provided keyword arguments.
        4. Assert that the attributes of the instantiated object
        match the provided values.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        nation = Country(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(nation.id, "345")
        self.assertEqual(nation.created_at, date)
        self.assertEqual(nation.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that Country instantiation raises a TypeError
        when any of the keyword arguments
        (id, created_at, updated_at) is set to None.
        """
        with self.assertRaises(TypeError):
            Country(id=None, created_at=None, updated_at=None)
