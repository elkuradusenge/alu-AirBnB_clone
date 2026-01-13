#!/usr/bin/python3
"""Unittest module for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
