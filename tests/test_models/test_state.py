#!/usr/bin/python3
'''Defines unittest for the State class'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''Defines testcases for the State class'''

    def test_initialization(self):
        '''Ensures objects of the State class are instantiated
        correctly'''

        s1 = State()
        self.assertTrue(len(s1.__dict__) == 3)

    def test_to_dict(self):
        '''Ensures the to_dict method works as expected
        on instances of State'''

        s2 = State()
        s2_dict = s2.to_dict()
        self.assertTrue(len(s2_dict) == 4)


if __name__ == "__main__":
    unittest.main()
