#!/usr/bin/python3
"""
unittest sequences for Place.py.

Sequences:
    TestPlace_instantiation
"""

import Model
import unittest
from datetime import datetime
from time import sleep
from Model.Place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """
        Test that instantiates a Place object with no arguments.
        It asserts that the type of the instantiated object is Place.
        """
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of Place is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(Place(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the id attribute
        of the Place class is of type str.

        It creates an instance of the Place class
        and checks if the type of its id attribute is str.
        """
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """
        Test case to verify that the `created_at` attribute
        of the Place class is of type datetime.
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the 'updated_at' attribute
        of the Place class is of type datetime.
        """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """
        Test if the city_id attribute is a public class attribute.

        This test checks if the city_id attribute
        of the Place class is a public class attribute.
        It verifies that the attribute is of type str, exists in the class's
        namespace, and is not present in the instance's dictionary.
        """
        locality = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(locality))
        self.assertNotIn("city_id", locality.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """
        Test case to verify that the user_id attribute
        is a public class attribute.

        It checks the following conditions:
        - The type of the user_id attribute is str.
        - The user_id attribute is present in the class's namespace.
        - The user_id attribute is not present in the instance's dictionary.
        """
        locality = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(locality))
        self.assertNotIn("user_id", locality.__dict__)

    def test_name_is_public_class_attribute(self):
        """
        Test case to verify that the 'name' attribute
        is a public class attribute.

        It checks if the 'name' attribute of
        the 'Place' class is of type 'str',
        if it is present in the 'locality' object's attributes,
        and if it is not present in the 'locality' object's
        dictionary (__dict__).
        """
        locality = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(locality))
        self.assertNotIn("name", locality.__dict__)

    def test_description_is_public_class_attribute(self):
        """
        Test case to verify that the 'description' attribute
        of the Place class is a public class attribute.

        It checks the following conditions:
        - The type of 'description' attribute is 'str'.
        - 'description' is present in the list of attributes
        returned by the 'dir' function for an instance of the Place class.
        - 'description' is not present in the instance's '__dict__' attribute.
        """
        locality = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(locality))
        self.assertNotIn("desctiption", locality.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """
        Test if the number_rooms attribute is a public class attribute.

        This test checks if the number_rooms attribute
        of the Place class is a public class attribute.
        It asserts that the type of number_rooms is int,
        checks if number_rooms is present in the
        instance's dir() and asserts that number_rooms
        is not present in the instance's __dict__.
        """
        locality = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(locality))
        self.assertNotIn("number_rooms", locality.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """
        Test case to verify that 'number_bathrooms'
        is a public class attribute.

        It checks if the type of 'number_bathrooms' is 'int',
        if 'number_bathrooms' is present in the 'dir' of
        an instance of the 'Place' class,
        and if 'number_bathrooms' is not present in the '__dict__' of
        the 'Place' instance.
        """
        locality = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(locality))
        self.assertNotIn("number_bathrooms", locality.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """
        Test case to verify that max_guest is a public class attribute.

        It checks the following assertions:
        - The type of Place.max_guest is int.
        - "max_guest" is present in the attributes of an instance of Place.
        - "max_guest" is not present in the instance dictionary of Place.
        """
        locality = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(locality))
        self.assertNotIn("max_guest", locality.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """
        Test case to verify that the `price_by_night` attribute of
        the `Place` class is a public class attribute.

        It checks the following assertions:
        - The type of `Place.price_by_night` is `int`.
        - The attribute `price_by_night` is present in the `Place` class.
        - The attribute `price_by_night` is not present in
        the instance's `__dict__`.

        This test ensures that the `price_by_night` attribute
        is accessible as a class attribute and not as an instance attribute.
        """
        locality = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(locality))
        self.assertNotIn("price_by_night", locality.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """
        Test case to verify that the `latitude` attribute
        is a public class attribute.

        It checks the following conditions:
        - The `latitude` attribute of the `Place` class is of type `float`.
        - The `latitude` attribute is present
        in the `locality` object's namespace.
        - The `latitude` attribute is not present
        in the `locality` object's `__dict__`.
        """
        locality = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(locality))
        self.assertNotIn("latitude", locality.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """
        Test case to verify that the 'longitude' attribute
        is a public class attribute.

        It checks that the 'longitude' attribute exists
        in the class's namespace,
        but not in the instance's dictionary.
        It also verifies that the type of 'longitude' is float.
        """
        locality = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(locality))
        self.assertNotIn("longitude", locality.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """
        Test case to verify that amenity_ids is a public class attribute.

        It checks if the type of Place.amenity_ids is a list,
        if "amenity_ids" is present in the attributes of an instance of Place,
        and if "amenity_ids" is not present in the instance's __dict__.
        """
        locality = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(locality))
        self.assertNotIn("amenity_ids", locality.__dict__)

    def test_two_places_unique_ids(self):
        """
        Test case to verify that two instances of
        the Place class have unique IDs.
        """
        locality1 = Place()
        locality2 = Place()
        self.assertNotEqual(locality1.id, locality2.id)

    def test_two_places_different_created_at(self):
        """
        Test case to verify that two Place instances
        have different 'created_at' values.
        """
        locality1 = Place()
        sleep(0.05)
        locality2 = Place()
        self.assertLess(locality1.created_at, locality2.created_at)

    def test_two_places_different_updated_at(self):
        """
        Test case to check if two places have different updated_at values.
        """
        locality1 = Place()
        sleep(0.05)
        locality2 = Place()
        self.assertLess(locality1.updated_at, locality2.updated_at)

    def test_str_representation(self):
        """
        Test the __str__ representation of the Place class.

        This test verifies that the __str__ method of
        the Place class returns the expected string representation.
        It checks if the string contains the correct ID,
        'id' attribute, 'created_at' attribute, and 'updated_at' attribute.
        """
        date = datetime.today()
        dt_repr = repr(date)
        locality = Place()
        locality.id = "123456"
        locality.created_at = locality.updated_at = date
        localitystr = locality.__str__()
        self.assertIn("[Place] (123456)", localitystr)
        self.assertIn("'id': '123456'", localitystr)
        self.assertIn("'created_at': " + dt_repr, localitystr)
        self.assertIn("'updated_at': " + dt_repr, localitystr)

    def test_args_unused(self):
        """
        Test case to check if any unused arguments are present
        in the Place object.

        It asserts that None is not present in the values of
        the object's dictionary.
        """
        locality = Place(None)
        self.assertNotIn(None, locality.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test case to verify the instantiation of
        a Place object with keyword arguments.

        This test case checks if a Place object is
        instantiated correctly when provided with keyword arguments.
        It verifies that the id, created_at, and updated_at attributes
        of the object are set correctly.

        Steps:
        1. Get the current date and time using
        the datetime.today() method.
        2. Convert the date to ISO format using the isoformat() method.
        3. Create a Place object with the id, created_at,
        and updated_at attributes set using the keyword arguments.
        4. Assert that the id attribute of the object is
        equal to the provided id.
        5. Assert that the created_at attribute of the object
        is equal to the current date and time.
        6. Assert that the updated_at attribute of the object
        is equal to the current date and time.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        locality = Place(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(locality.id, "345")
        self.assertEqual(locality.created_at, date)
        self.assertEqual(locality.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that instantiation of the Place class
        raises a TypeError when
        provided with None values for
        the id, created_at, and updated_at attributes.
        """
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)
