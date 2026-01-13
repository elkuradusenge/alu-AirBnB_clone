#!/usr/bin/python3
"""Unittest module for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test fixtures"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test basic instantiation"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method"""
        obj = BaseModel()
        string = str(obj)
        self.assertIn("[BaseModel]", string)
        self.assertIn(obj.id, string)

    def test_save_method(self):
        """Test save method updates updated_at"""
        obj = BaseModel()
        old_updated = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated, obj.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
