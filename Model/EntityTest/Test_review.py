#!/usr/bin/python3
"""
unittest sequences for Review.py.

Sequences:
    TestReview_instantiation
"""

import Model
import unittest
from datetime import datetime
from time import sleep
from Model.Review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        """
        Test case to verify that Review class
        can be instantiated with no arguments.
        """
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of Review is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(Review(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the id attribute
        of Review is of type str.
        """
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """
        Test case to verify that the `created_at` attribute
        of the Review class is of type datetime.
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the `updated_at` attribute
        of the Review class is of type datetime.
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """
        This test checks if the place_id attribute
        of the Review class is a public class attribute.
        It verifies that the attribute is of type str,
        exists in the class's namespace, and is not present
        in the instance's dictionary.
        """
        note = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(note))
        self.assertNotIn("place_id", note.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """
        It checks if the type of Review.user_id is str,
        if "user_id" is present in the dir(note),
        and if "user_id" is not present in the note.__dict__.
        """
        note = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(note))
        self.assertNotIn("user_id", note.__dict__)

    def test_text_is_public_class_attribute(self):
        """
        This test checks that the 'text' attribute of
        the Review class is a public class attribute
        by performing the following assertions:
        - The type of Review.text is equal to str.
        - The 'text' attribute is present in the dir() of
        an instance of the Review class.
        - The 'text' attribute is not present in the __dict__ of
        an instance of the Review class.
        """
        note = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(note))
        self.assertNotIn("text", note.__dict__)

    def test_two_reviews_unique_ids(self):
        """
        Test case to verify that two reviews have unique IDs.
        """
        note1 = Review()
        note2 = Review()
        self.assertNotEqual(note1.id, note2.id)

    def test_two_reviews_different_created_at(self):
        """
        Test case to verify that two reviews
        have different created_at timestamps.
        """
        note1 = Review()
        sleep(0.05)
        note2 = Review()
        self.assertLess(note1.created_at, note2.created_at)

    def test_two_reviews_different_updated_at(self):
        """
        Test case to verify that two reviews
        have different updated_at values.
        """
        note1 = Review()
        sleep(0.05)
        note2 = Review()
        self.assertLess(note1.updated_at, note2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of the Review object.

        This method verifies that the __str__ method of
        the Review class returns the expected string representation.
        It checks if the string contains the Review ID,
        'id' attribute, 'created_at' attribute,
        and 'updated_at' attribute.
        """
        date = datetime.today()
        date_repr = repr(date)
        note = Review()
        note.id = "123456"
        note.created_at = note.updated_at = date
        notestr = note.__str__()
        self.assertIn("[Review] (123456)", notestr)
        self.assertIn("'id': '123456'", notestr)
        self.assertIn("'created_at': " + date_repr, notestr)
        self.assertIn("'updated_at': " + date_repr, notestr)

    def test_args_unused(self):
        """
        Test case to verify that no unused arguments
        are present in the Review object.

        This test creates a Review object with no arguments
        and checks that none of the values
        in the object's dictionary are None.
        """
        note = Review(None)
        self.assertNotIn(None, note.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        This test case checks if a Review object can be instantiated
        correctly when providing keyword arguments.
        It verifies that the provided attributes
        match the expected values.

        Steps:
        1. Get the current date and time.
        2. Convert the date to ISO format.
        3. Create a Review object with the provided id,
        created_at, and updated_at values.
        4. Assert that the id attribute of the Review object
        matches the provided id.
        5. Assert that the created_at attribute of the Review object
        matches the current date.
        6. Assert that the updated_at attribute of the Review object
        matches the current date.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        note = Review(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(note.id, "345")
        self.assertEqual(note.created_at, date)
        self.assertEqual(note.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that Review instantiation
        raises a TypeError when provided with None values
        for id, created_at, and updated_at.
        """
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)
