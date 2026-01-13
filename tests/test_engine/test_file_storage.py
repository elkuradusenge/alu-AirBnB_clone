#!/usr/bin/python3
"""Unittest module for FileStorage class"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test if all() returns a dictionary"""
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test if new() correctly adds an object to __objects"""
        obj = BaseModel()
        storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test if save() creates the JSON file"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_loads_objects(self):
        """Test if reload() correctly loads objects from file"""
        obj = BaseModel()
        obj_id = obj.id
        storage.new(obj)
        storage.save()

        # Clear __objects to test reload
        storage._FileStorage__objects = {}
        storage.reload()

        key = f"BaseModel.{obj_id}"
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
