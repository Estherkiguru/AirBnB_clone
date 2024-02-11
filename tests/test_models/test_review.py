#!/usr/bin/python3
'''Defines unittests for the Review class'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''Defines test cases for the Review class'''

    def test_initialization(self):
        '''Ensures objects of the Review class are instantiated
        correctly'''

        r1 = Review()
        self.assertTrue(len(r1.__dict__) == 3)

    def test_to_dict(self):
        '''Ensures the to_dict method works as expected
        on instances of Review'''

        r2 = Review()
        r2_dict = r2.to_dict()
        self.assertTrue(len(r2_dict) == 4)


if __name__ == "__main__":
    unittest.main()
