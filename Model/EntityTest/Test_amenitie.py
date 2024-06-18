import unittest
from Model.Amenity import Amenity
import uuid, datetime

class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity("Swimming Pool")
        self.assertIsInstance(amenity.amenity_id, uuid.UUID)
        self.assertEqual(amenity.name, "Swimming Pool")
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()