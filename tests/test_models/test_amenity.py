#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from class amenity"""

    amenity = Amenity()

    def test_class(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.amenity)), "<class 'models.amenity.Amenity'>")

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_types(self):
        """tests attribute type"""
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
