#!/usr/bin/python3

import unittest
from datetime import datetime
from Class.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_init(self):
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.review_id, str)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.content, "")
        self.assertEqual(self.review.created_at, self.review.updated_at)

if __name__ == '__main__':
    unittest.main()