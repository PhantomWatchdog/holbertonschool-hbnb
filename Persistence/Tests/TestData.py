import unittest
import os
from Persistence.DataManager import ConcreteDataManager
from Model.User import User
from app import app
from flask_sqlalchemy import SQLAlchemy
import tempfile

class TestDataManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup that runs once before all tests
        cls.original_use_database = os.getenv('USE_DATABASE')
    
    @classmethod
    def tearDownClass(cls):
        # Cleanup that runs once after all tests
        if cls.original_use_database is not None:
            os.environ['USE_DATABASE'] = cls.original_use_database
        else:
            del os.environ['USE_DATABASE']

    def setUp(self):
        # Setup that runs before each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_manager = ConcreteDataManager()
        if not self.data_manager.use_database:
            self.data_manager.storage_path = self.temp_dir.name  # Assuming DataManager can use a custom path

    def tearDown(self):
        # Cleanup that runs after each test
        self.temp_dir.cleanup()

    def test_create_user_db(self):
        with app.app_context():  # Push an application context
            user = User(email="testuser@example.com", first_name="Test", last_name="User", password="securepassword123")
            self.data_manager.save(user)
            # Assuming DataManager has a method to retrieve all users
            self.assertIn(user, self.data_manager.get_all(User))

    def test_create_user_file(self):
        os.environ['USE_DATABASE'] = 'False'
        self.data_manager.use_database = False
        user = User(email="testuser@example.com", first_name="Test2", last_name="User2", password="securepassword123")
        self.data_manager.save(user)
        self.assertIn(user, self.data_manager.get_all(User))

# Additional tests for Read, Update, Delete, Relationships, and Dynamic Switching

if __name__ == '__main__':
    unittest.main()