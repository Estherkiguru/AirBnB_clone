#!/usr/bin/python3
"""test cases for class user"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """defines test cases for the User class"""
    def test_check_attributes(self):
        """Checks if the default atrributes are empty strings"""
        u1 = User()
        self.assertEqual(len(u1.email), 0)
        self.assertEqual(len(u1.password), 0)
        self.assertEqual(len(u1.first_name), 0)
        self.assertEqual(len(u1.last_name), 0)

    def test_to_dict(self):
        """checks if to_dict method functions correctly"""
        u2 = User()
        u2_dict = u2.to_dict()
        self.assertTrue(len(u2_dict) == 4)
        




if __name__ == "__main__":
    unittest.main()
