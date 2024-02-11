#!/usr/bin/python3
'''Defines unittests for the class Place'''
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''Defines test cases for the Place class'''

    def test_initialization(self):
        '''Ensures objects of the Place class are instantiated
        correctly'''

        p1 = Place()
        self.assertTrue(len(p1.__dict__) == 3)

    def test_to_dict(self):
        '''Ensures the to_dict method works as expected
        on instances of Place'''

        p2 = Place()
        p2_dict = p2.to_dict()
        self.assertTrue(len(p2_dict) == 4)


if __name__ == "__main__":
    unittest.main()
