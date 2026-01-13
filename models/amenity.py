#!/usr/bin/python3
"""Amenity module - defines Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class - represents an amenity

    Attributes:
        name (str): Amenity name
    """

    name = ""
