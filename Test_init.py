#!/usr/bin/python3
"""Unittest for base __init__ module"""

import unittest
from Model.EntityStorage.Storage import Storage


class Test_file_storage(unittest.TestCase):
    """test for file storage instance"""
    def test_instance(self):
        storage = Storage()
        self.assertIsInstance(storage, Storage)


if __name__ == '__main__':
    unittest.main()