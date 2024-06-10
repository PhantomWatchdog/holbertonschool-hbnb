import unittest, os
from Model.Base_Model import BaseModel
from Model.user import User
from Model.EntityStorage.Storage import Storage

class StorageTests(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()

    def test_all(self):
        # Test if all() returns the correct dictionary
        self.assertEqual(self.storage.all(), {})

        # Test if all() returns the correct dictionary after adding objects
        user = User()
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.{}".format(user.id): user})

    def test_new(self):
        # Test if new() adds the object to __objects dictionary
        user = User()
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.{}".format(user.id): user})

    def test_save(self):
        # Test if save() serializes __objects to the JSON file
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Check if the JSON file exists
        self.assertTrue(os.path.exists(self.storage.__file_path))

    def test_reload(self):
        # Test if reload() deserializes the JSON file to __objects
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Clear __objects and reload from the JSON file
        self.storage.__objects = {}
        self.storage.reload()

        # Check if the object is loaded correctly
        self.assertEqual(self.storage.all(), {"User.{}".format(user.id): user})

if __name__ == '__main__':
    unittest.main()