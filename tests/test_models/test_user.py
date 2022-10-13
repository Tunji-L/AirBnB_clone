#!/usr/bin/python3
"""
unittest for user
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class UserInstance(unittest.TestCase):
    """
    Test instance and method of user
    """

    user = User()

    def test_usertype(self):
        """test if user exists"""
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if user is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def testHasAttributes(self):
        """verify if attributes exists"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_types(self):
        """test attributes type"""
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
