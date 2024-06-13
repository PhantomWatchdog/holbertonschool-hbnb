#!/usr/bin/python3
"""
unittest sequences for City.py.

Sequences:
    TestCity_instantiation
"""
import Model
import unittest
from datetime import datetime
from time import sleep
from Model.City import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """
        Test case to verify that City class
        can be instantiated with no arguments.
        """
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of City is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(City(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the id attribute
        of the City class is of type str.
        """
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """
        Test case to check if the 'created_at' attribute
        of the City class is of type datetime.
        """
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the 'updated_at' attribute
        of the City class is of type datetime.
        """
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """
        Test if the state_id attribute is a public class attribute.
        """
        Town = City()
        self.assertEqual(str, type(City.country_id))
        self.assertIn("country_id", dir(Town))
        self.assertNotIn("country_id", Town.__dict__)

    def test_name_is_public_class_attribute(self):
        """
        Test case to verify that the 'name' attribute
        is a public class attribute.

        It checks the following conditions:
        - The type of 'City.name' is 'str'.
        - 'name' is present in the list of attributes
        returned by the 'dir' function on an instance of 'City'.
        - 'name' is not present in the '__dict__' attribute
        of an instance of 'City'.
        """
        Town = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(Town))
        self.assertNotIn("name", Town.__dict__)

    def test_two_cities_unique_ids(self):
        """
        Test case to verify that two City instances have unique IDs.
        """
        Town1 = City()
        Town2 = City()
        self.assertNotEqual(Town1.id, Town2.id)

    def test_two_cities_different_created_at(self):
        """
        Test if two cities have different 'created_at' timestamps.
        """
        Town1 = City()
        sleep(0.05)
        Town2 = City()
        self.assertLess(Town1.created_at, Town2.created_at)

    def test_two_cities_different_updated_at(self):
        """
        Test case to verify that the 'updated_at' attribute
        of two City instancesis different,
        with the second instance being created after a small delay.
        """
        Town1 = City()
        sleep(0.05)
        Town2 = City()
        self.assertLess(Town1.updated_at, Town2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of the City object.

        It asserts that the string representation includes the following:
        - The object type '[City]'
        - The object's ID
        - The object's 'id' attribute
        - The object's 'created_at' attribute
        - The object's 'updated_at' attribute
        """
        date = datetime.today()
        date_repr = repr(date)
        Town = City()
        Town.id = "123456"
        Town.created_at = Town.updated_at = date
        Townstr = Town.__str__()
        self.assertIn("[City] (123456)", Townstr)
        self.assertIn("'id': '123456'", Townstr)
        self.assertIn("'created_at': " + date_repr, Townstr)
        self.assertIn("'updated_at': " + date_repr, Townstr)

    def test_args_unused(self):
        """
        Test case to verify that the City object
        does not contain any unused arguments.
        """
        Town = City(None)
        self.assertNotIn(None, Town.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test case to verify the instantiation of City object
        with keyword arguments.

        Steps:
        1. Create a City object using keyword arguments.
        2. Verify that the attributes of the instantiated object
        match the provided values.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        Town = City(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Town.id, "345")
        self.assertEqual(Town.created_at, date)
        self.assertEqual(Town.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that City instantiation raises a TypeError when
        provided with None values for id, created_at, and updated_at.
        """
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)
