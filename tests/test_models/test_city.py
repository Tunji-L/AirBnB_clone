#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from models.city import City
from models.base_model import BaseModel
import datetime


class TestCity(unittest.TestCase):
    """Tests instances and methods from class city"""

    city = City()

    def test_class(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.city, BaseModel)

    def testHasAttributes(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_types(self):
        """tests attributes type"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
