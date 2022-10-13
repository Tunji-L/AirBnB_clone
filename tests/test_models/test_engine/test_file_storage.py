#!/usr/bin/python3
"""File storage unittest"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    Test File storage
    """
    bm = BaseModel()

    def testFileStorageInstance(self):
        """Test instantiation from FileStorage"""
        self.assertIsInstance(storage, FileStorage)

    def testFilePath(self):
        if os.path.exists("file.json"):
            os.remove("./file.json")
        self.bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def testObject(self):
        """test object is not empty after instantiation"""
        

if __name__ == '__main__':
    unittest.main()

