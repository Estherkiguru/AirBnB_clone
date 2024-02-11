#!/usr/bin/python3
"""test cases for class Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class for test the default attributes in class Amenity"""
    def test_amenity_attributes(self):
        """checks if the default attributes are empty"""
        amn1 = Amenity()
        self.assertEqual(len(amn1.name), 0)

    def test_to_dict(self):
        """checks if the to_dict method is handled properly"""
        amn2 = Amenity()
        amn2_dict = amn2.to_dict()
        self.assertTrue(len(amn2_dict) == 4)


if __name__ == "__main__":
    unittest.main()
