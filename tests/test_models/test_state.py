#!/usr/bin/python3
"""Unittest module for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
