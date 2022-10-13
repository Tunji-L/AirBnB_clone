#!/usr/bin/python3
"""
Unittest for state.py
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """ Tests instances and methods from class State """

    state = State()

    def test_class(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def test_state_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def testHasAttributes(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
