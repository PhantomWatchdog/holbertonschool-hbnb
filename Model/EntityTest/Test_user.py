import unittest
from datetime import datetime, timedelta
from Model.User import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("test@example.com", "John", "Doe", "password")

    def test_user_attributes(self):
        self.assertIsInstance(self.user.user_id, str)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.password, "password")
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(self.user.places, [])

    def test_user_id_uniqueness(self):
        other_user = User("other@example.com", "Jane", "Smith", "password")
        self.assertNotEqual(self.user.user_id, other_user.user_id)

    def test_user_created_at(self):
        now = datetime.now()
        self.assertAlmostEqual(self.user.created_at, now, delta=timedelta(seconds=1))

    def test_user_updated_at(self):
        now = datetime.now()
        self.assertAlmostEqual(self.user.updated_at, now, delta=timedelta(seconds=1))

    def test_user_places(self):
        place1 = "Place 1"
        place2 = "Place 2"
        self.user.places.append(place1)
        self.user.places.append(place2)
        self.assertEqual(self.user.places, [place1, place2])

if __name__ == '__main__':
    unittest.main()