#!/usr/bin/python3

import unittest
import os
from datetime import datetime
from Class.user import User
from Class.Storage.Entity_storage import Storage


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()

    def tearDown(self):
        if os.path.exists(self.storage._Storage__file_path):
            os.remove(self.storage._Storage__file_path)

    def test_all_new_save_reload(self):
        user_data = {
            "id": "d30e3d68-24f6-48e6-9627-88e4925f6014",
            "created_at": "2024-06-13T10:04:53.824622",
            "updated_at": "2024-06-13T10:04:53.824628",
            "first_name": "Test",
            "last_name": "User1",
            "password": "testpassword1",
            "mail": "test.user1@example.com"
        }

        user = User(**user_data)
        
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.d30e3d68-24f6-48e6-9627-88e4925f6014": user})

        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._Storage__file_path))

        self.storage._Storage__objects = {}
        self.storage.reload()
        self.assertEqual(self.storage.all(), {"User.d30e3d68-24f6-48e6-9627-88e4925f6014": user})

if __name__ == '__main__':
    unittest.main()