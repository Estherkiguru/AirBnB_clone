#!/usr/bin/python3
'''Defines a unit test for the base_model module'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Defines test cases for the BaseModel class'''

    def test_correct_initialisation(self):
        '''Ensures all class attributes are correctly initialised
        when kwargs is empty'''

        b1 = BaseModel()
        self.assertEqual(len(b1.__dict__), 3)
        b1.name = "John"
        self.assertEqual(len(b1.__dict__), 4)

    def test_kwargs_arguments(self):
        '''Ensures kwargs is handled correctly by the dunder init'''

        b2 = BaseModel()
        b2.name = "My first Model"
        b2.my_number = 89
        b2_json = b2.to_dict()
        b2_new = BaseModel(**b2_json)
        self.assertTrue(len(b2_new.__dict__) == 5)

    def test_to_dict(self):
        '''Ensures that the to_dict method of BaseModel works
        as expected'''

        b3 = BaseModel()
        b3_dict = b3.to_dict()
        self.assertTrue(len(b3_dict) == 4)
        self.assertTrue("__class__" in b3_dict)

    def test_to_dict_datetime_conversion(self):
        '''Ensures to_dict converts the two datetime attributes
        to strings when invoked'''

        b4 = BaseModel()
        b4_dict = b4.to_dict()
        self.assertTrue(isinstance(b4_dict["created_at"], str))
        self.assertTrue(isinstance(b4_dict["updated_at"], str))


if __name__ == "__main__":
    unittest.main()
