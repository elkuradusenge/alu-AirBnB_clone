#!/usr/bin/python3
"""Review module - defines Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class - represents a review

    Attributes:
        place_id (str): Place ID
        user_id (str): User ID
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
