#!/usr/bin/python3
"""
unittest sequences for Base_Model.py.

Sequences:
    TestBaseModel_instantiation
"""

import Model
import unittest
from datetime import datetime
from time import sleep
from Model.Base_Model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """
        Test that instantiating BaseModel with
        no arguments creates an instance of BaseModel.
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """
        Test if a new instance of BaseModel is stored
        in the objects dictionary of the Storage class.
        """
        self.assertIn(BaseModel(), Model.Storage.all().values())

    def test_id_is_public_str(self):
        """
        Test case to verify that the id attribut
        of BaseModel is a string.

        It creates a new instance of BaseModel
        and checks if the type of the id attribute is a string.
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """
        Test that the `created_at` attribute of the BaseModel
        instance is of type `datetime`.
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test case to verify that the `updated_at` attribut
        of the BaseModel class is of type datetime.
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """
        Test case to verify that two instances of
        the BaseModel class have unique IDs.
        """
        Base1 = BaseModel()
        Base2 = BaseModel()
        self.assertNotEqual(Base1.id, Base2.id)

    def test_two_models_different_created_at(self):
        """
        Test that two BaseModel instances have
        different 'created_at' values.
        """
        Base1 = BaseModel()
        sleep(0.05)
        Base2 = BaseModel()
        self.assertLess(Base1.created_at, Base2.created_at)

    def test_two_models_different_updated_at(self):
        """
        Test case to verify that two BaseModel instances
        have different updated_at values.
        """
        Base1 = BaseModel()
        sleep(0.05)
        Base2 = BaseModel()
        self.assertLess(Base1.updated_at, Base2.updated_at)

    def test_str_representation(self):
        """
        This test verifies that the __str__ method of
        the BaseModel class returns the expected string representation.
        It checks if the string contains the BaseModel
        class name, the id attribute, the created_at attribute,
        and the updated_at attribute.
        """
        date = datetime.today()
        date_repr = repr(date)
        Base = BaseModel()
        Base.id = "123456"
        Base.created_at = Base.updated_at = date
        Basestr = Base.__str__()
        self.assertIn("[BaseModel] (123456)", Basestr)
        self.assertIn("'id': '123456'", Basestr)
        self.assertIn("'created_at': " + date_repr, Basestr)
        self.assertIn("'updated_at': " + date_repr, Basestr)

    def test_args_unused(self):
        """
        Test case to check if the BaseModel instance
        does not contain any unused arguments.
        """
        Base = BaseModel(None)
        self.assertNotIn(None, Base.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        This test case checks if the BaseModel
        class can be instantiated with keyword arguments.
        It verifies that the id, created_at,
        and updated_at attributes of the instantiated object
        match the provided values.

        Steps:
        1. Create a datetime object representing the current date and time.
        2. Convert the datetime object to an ISO formatted string.
        3. Instantiate a BaseModel object with id,
        created_at, and updated_at keyword arguments.
        4. Assert that the id attribute of the instantiated object
        matches the provided id value.
        5. Assert that the created_at attribute of the instantiated object
        matches the provided date.
        6. Assert that the updated_at attribute of the instantiated object
        matches the provided date.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        Base = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Base.id, "345")
        self.assertEqual(Base.created_at, date)
        self.assertEqual(Base.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        """
        Test case to verify that instantiating the BaseModel
        class with None kwargs raises a TypeError.
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """
        Test case to verify the instantiation of BaseModel
        with arguments and keyword arguments.

        It creates an instance of BaseModel
        with the following arguments and keyword arguments:
        - id: "345"
        - created_at: current date and time
        - updated_at: current date and time

        The test asserts that the instance's id,
        created_at, and updated_at attributes are set correctly.
        """
        date = datetime.today()
        date_iso = date.isoformat()
        Base = BaseModel("12", id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Base.id, "345")
        self.assertEqual(Base.created_at, date)
        self.assertEqual(Base.updated_at, date)
