#!/usr/bin/python3
"""Unittest module for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
