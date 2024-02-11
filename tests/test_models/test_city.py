#!/usr/bin/python3
"""test cases for class City"""
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """class for test the default attributes in class City"""
    def test_city_attributes(self):
        """checks if the default attributes are empty"""
        c1 = City()
        self.assertEqual(len(c1.state_id), 0)
        self.assertEqual(len(c1.name), 0)

    def test_to_dict(self):
        """checks if the to_dict method is handled properly"""
        c2 = City()
        c2_dict = c2.to_dict()
        self.assertTrue(len(c2_dict) == 4)


if __name__ == "__main__":
    unittest.main()
