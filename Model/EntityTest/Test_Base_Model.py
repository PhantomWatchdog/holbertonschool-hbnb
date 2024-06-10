#!/usr/bin/python3
"""Unittest for base model class"""

import unittest
import uuid
from datetime import datetime, timedelta
from Model.Base_Model import BaseModel

""" class test DefineBaseModel """


class TestDefineBaseModel(unittest.TestCase):

    def test_instantiation(self):
        """ test new instance of Base model """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_str(self):
        """ test new instance of Base model with string """
        my_model = BaseModel("Model")
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_int(self):
        """ test new instance of Base model with integer """
        my_model = BaseModel(70)
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_dict(self):
        """ Test instantiation with a dictionary """
        my_dict = {"key": "value"}
        my_model = BaseModel(my_dict)
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_list(self):
        """ Test instantiation with a list """
        my_list = [1, 2, 3]
        my_model = BaseModel(my_list)
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_float(self):
        """ Test instantiation with a float """
        my_float = 3.14
        my_model = BaseModel(my_float)
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_none(self):
        """ Test instantiation with None """
        my_model = BaseModel(None)
        self.assertIsInstance(my_model, BaseModel)

    def test_instantiation_tuple(self):
        """ test new instance of Base model with tuple """
        my_model = BaseModel((10, 4, 20))
        self.assertIsInstance(my_model, BaseModel)

    def test_attribute_name(self):
        """ test new instance with name """
        my_model = BaseModel()
        my_model.name = "My First Model"
        self.assertEqual(my_model.name, "My First Model")

    def test_attribute_name_integer(self):
        """ test new instance with name integer """
        my_model = BaseModel()
        my_model.name = 10
        self.assertEqual(my_model.name, 10)

    def test_attribute_name_float(self):
        """ test new instance with name float"""
        my_model = BaseModel()
        my_model.name = 4.5
        self.assertEqual(my_model.name, 4.5)

    def test_attribute_name_dict(self):
        """ test new instance with name dictionnary"""
        my_model = BaseModel()
        my_model.name = {"key: value"}
        self.assertEqual(my_model.name, {"key: value"})

    def test_attribute_name_list(self):
        """ test new instance with name list """
        my_model = BaseModel()
        my_model.name = [10, 5, 12]
        self.assertEqual(my_model.name, [10, 5, 12])

    def test_attribute_name_tuple(self):
        """ test new instance with name tuple """
        my_model = BaseModel()
        my_model.name = (10, 5, 12)
        self.assertEqual(my_model.name, (10, 5, 12))

    def test_attribute_name_none(self):
        """ test new instance with name empty """
        my_model = BaseModel()
        my_model.name = None
        self.assertEqual(my_model.name, None)

    def test_attribute_number(self):
        """ test new instance with number """
        my_model = BaseModel()
        my_model.number = 70
        self.assertEqual(my_model.number, 70)

    def test_attribute_number_str(self):
        """ test new instance with string """
        my_model = BaseModel()
        my_model.number = "Nassim"
        self.assertEqual(my_model.number, "Nassim")

    def test_attribute_number_float(self):
        """ test new instance with float """
        my_model = BaseModel()
        my_model.number = 12.5
        self.assertEqual(my_model.number, 12.5)

    def test_attribute_number_list(self):
        """ test new instance with list """
        my_model = BaseModel()
        my_model.number = [15, 12, 23]
        self.assertEqual(my_model.number, [15, 12, 23])

    def test_attribute_number_dict(self):
        """ test new instance with dictionnary """
        my_model = BaseModel()
        my_model.number = {"key: value"}
        self.assertEqual(my_model.number, {"key: value"})

    def test_attribute_number_tuple(self):
        """ test new instance with tuple """
        my_model = BaseModel()
        my_model.number = (10, 20, 30)
        self.assertEqual(my_model.number, (10, 20, 30))

    def test_attribute_number_none(self):
        """ test new instance with none """
        my_model = BaseModel()
        my_model.number = None
        self.assertEqual(my_model.number, None)

    def test_date_creation(self):
        """ test date new instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLessEqual
        (my_model.created_at, current_time + timedelta(seconds=1))

    def test_hour_creation(self):
        """ test hour new instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertEqual(my_model.created_at.date(), current_time.date())

    def test_hour_precision_creation(self):
        """ test hour new instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLessEqual
        (abs(current_time - my_model.created_at), timedelta(seconds=1))

    def test_date_update(self):
        """ test date update instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLessEqual
        (my_model.updated_at, current_time + timedelta(seconds=1))

    def test_hour_update(self):
        """ test hour update instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertEqual
        (my_model.updated_at.date(), current_time.date())

    def test_hour_update_precision(self):
        """ test hour update instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLessEqual
        (abs(current_time - my_model.updated_at), timedelta(seconds=1))

    def test_id(self):
        """ test creation id """
        model = BaseModel()

        self.assertTrue(isinstance(model.id, str))
        self.assertTrue(len(model.id) > 0)

    def test_id_unique(self):
        """ test creation id """
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertTrue(isinstance(model1.id, str))
        self.assertTrue(isinstance(model2.id, str))
        self.assertTrue(len(model1.id) > 0)
        self.assertTrue(len(model2.id) > 0)

        self.assertNotEqual(model1.id, model2.id)

    def test_id_stability(self):
        """ test id stability after re-instantacion of an instance """
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertTrue(isinstance(model1.id, str))
        self.assertTrue(isinstance(model2.id, str))
        self.assertTrue(len(model1.id) > 0)
        self.assertTrue(len(model2.id) > 0)

        model1_id = model1.id
        self.assertEqual(model1_id, model1.id)


class TestStrBaseModel(unittest.TestCase):
    def test_str(self):
        """ test representation to a string """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.number = 5

        str_representation = str(my_model)

        expected_str = "[BaseModel] ({}) {}".format
        (my_model.id, my_model.__dict__)

    def test_str_no_attributes(self):
        """ test representation to a string
        without attributes"""
        my_model = BaseModel()
        str_representation = str(my_model)
        expected_str = "[BaseModel] ({}) {}".format
        (my_model.id, {})

    def test_str_one_attribute(self):
        """Test string representation with one attribute"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        expected_str = "[BaseModel] ({}) {}".format
        (my_model.id, {'name': 'Test Model'})

    def test_str_special_attributes(self):
        """Test string representation with special attributes"""
        my_model = BaseModel()
        my_model.__dict__["__class__"] = 'TestClass'
        expected_str = "[BaseModel] ({}) {}".format
        (my_model.id, my_model.__dict__)


class TestSaveBaseModel(unittest.TestCase):
    def test_save_updated(self):
        """ test updates the public instance attribute
        updated_at with the current datetime """
        my_model = BaseModel()
        current_time = datetime.now()
        my_model.save()
        self.assertLessEqual
        (abs(current_time - my_model.updated_at), timedelta(seconds=1))

    def test_save_updated_hour(self):
        """ test updates hour with the current datetime """
        my_model = BaseModel()
        current_time = datetime.now()
        my_model.save()
        self.assertEqual
        (my_model.updated_at.date(), current_time.date())

    def test_save_updated_hour_precision(self):
        """ test updates hour with precision the current datetime """
        my_model = BaseModel()
        current_time = datetime.now()
        my_model.save()
        self.assertLessEqual
        (abs(current_time - my_model.updated_at), timedelta(seconds=1))


class TestSerializationBaseModel(unittest.TestCase):
    def test_to_dict(self):
        """ test serializes object BaseModel to dict """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)


class TestBaseModelInit(unittest.TestCase):
    """test for base model class"""
    def test_no_kwargs(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_with_kwargs(self):
        my_model = BaseModel(name="My First Model", value=89)
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.value, 89)

    def test_created_at_updated_at_kwargs(self):
        my_model = BaseModel(created_at=datetime.now(),
                            updated_at=datetime.now())
        self.assertLessEqual(abs(datetime.now() - my_model.created_at),
                            timedelta(seconds=1))
        self.assertLessEqual(abs(datetime.now() - my_model.updated_at),
                            timedelta(seconds=1))

    def test_ignore_class_key(self):
        my_model = BaseModel(__class__="My Class")
        self.assertNotIn("__class__", my_model.__dict__)


if __name__ == '__main__':
    unittest.main()