#!/usr/bin/python3
"""
This file is the unit test for the base model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    unit test for base model
    """
    bm = BaseModel()

    def test_BaseModel(self):
        """
        Test the attribute values of BaseModel
        """
        self.bm.name = 'School'
        self.bm.number = 89
        self.assertEqual(self.bm.created_at, self.bm.updated_at)
        self.bm.save()
        bm_json = self.bm.to_dict()

        self.assertEqual(self.bm.name, bm_json['name'])
        self.assertEqual(self.bm.number, bm_json['number'])
        self.assertEqual('BaseModel', bm_json['__class__'])
        self.assertEqual(self.bm.id, bm_json['id'])

    def test_init(self):
        """
        test the class init method
        """

        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        """
        testing the output of the class
        """

        self.assertEqual(self.bm.__class__.__name__, "BaseModel")

    def test_save(self):
        """
        testing save method
        """

        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)
        self.assertIsInstance(self.bm.updated_at, datetime)
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_to_dict(self):
        """
        testing to_dict method
        """
        bm_json = self.bm.to_dict()
        self.assertIsInstance(bm_json['created_at'], str)
        self.assertIsInstance(bm_json['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
