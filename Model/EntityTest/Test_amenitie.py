#!/usr/bin/python3
"""
unittest sequences for Amenitie.py.

Sequences:
    TestAmenity_instantiation
"""

import Model
import unittest
from datetime import datetime
from time import sleep
from Model.Amenitie import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        """
        Test case to verify that an instance of the Amenity
        class is created when no arguments are passed.
        """
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """
        Test if a new instance of Amenity is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(Amenity(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test if the id attribute of the Amenity instance
        is of type str.
        """
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """
        Test case to verify that the 'created_at' attribute
        of the Amenity class is of type datetime.
        """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the `updated_at` attribute
        of the Amenity class is of type datetime.
        """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """
        Test case to verify that the 'name' attribute
        is a public class attribute.

        It checks the following assertions:
        - The type of 'name' attribute is 'str'.
        - The 'name' attribute is present in the list
        of attributes returned by the 'dir' function on an instance
        of 'Amenity' class.
        - The 'name' attribute is not present in the instance dictionary
        of 'amen' object.
        """
        amen = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_two_amenities_unique_ids(self):
        """
        Test case to verify that two instances
        of Amenity have unique IDs.
        """
        amen1 = Amenity()
        amen2 = Amenity()
        self.assertNotEqual(amen1.id, amen2.id)

    def test_two_amenities_different_created_at(self):
        """
        Test case to verify that two amenities
        have different 'created_at' timestamps.

        This ensures that each amenity object has a unique creation time.
        """
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.created_at, amen2.created_at)

    def test_two_amenities_different_updated_at(self):
        """
        Test case to verify that the 'updated_at' attribute
        of two Amenity objects is different,
        with the second object being created after a small delay.
        """
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.updated_at, amen2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of the Amenity object.

        This method creates an instance of the Amenity class
        and sets its attributes.
        It then calls the __str__ method of the Amenity object
        and checks if the expected string representation
        is present in the output.

        The expected string representation should contain
        the Amenity's ID, 'id' attribute, 'created_at' attribute,
        and 'updated_at' attribute.
        """
        date = datetime.today()
        date_repr = repr(date)
        amen = Amenity()
        amen.id = "123456"
        amen.created_at = amen.updated_at = date
        amenstr = amen.__str__()
        self.assertIn("[Amenity] (123456)", amenstr)
        self.assertIn("'id': '123456'", amenstr)
        self.assertIn("'created_at': " + date_repr, amenstr)
        self.assertIn("'updated_at': " + date_repr, amenstr)

    def test_args_unused(self):
        """
        Test case to verify that the Amenity object
        does not contain any unused arguments.
        """
        amen = Amenity(None)
        self.assertNotIn(None, amen.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test method for instantiating an Amenity object
        with keyword arguments.

        This method tests the instantiation of an Amenity object
        by passing keyword arguments.
        It verifies that the object is created correctly
        and that the attributes are set according
        to the provided arguments.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        amen = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amen.id, "345")
        self.assertEqual(amen.created_at, date)
        self.assertEqual(amen.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that instantiating the Amenity class
        with None kwargs raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)
