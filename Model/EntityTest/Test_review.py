import unittest
from datetime import datetime
from Model.Review import Review
import uuid

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user_id = "user123"
        self.place_id = "place456"
        self.rating = 4
        self.comment = "Great place!"
        self.review = Review(self.user_id, self.place_id, self.rating, self.comment)

    def test_review_attributes(self):
        self.assertIsInstance(self.review.review_id, uuid.UUID)
        self.assertEqual(self.review.user_id, self.user_id)
        self.assertEqual(self.review.place_id, self.place_id)
        self.assertEqual(self.review.rating, self.rating)
        self.assertEqual(self.review.comment, self.comment)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_timestamps(self):
        self.assertEqual(self.review.created_at, self.review.created_at)

    def test_review_update(self):
        new_rating = 5
        new_comment = "Amazing place!"
        self.review.rating = new_rating
        self.review.comment = new_comment
        self.assertEqual(self.review.rating, new_rating)
        self.assertEqual(self.review.comment, new_comment)
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

if __name__ == '__main__':
    unittest.main()