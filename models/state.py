#!/usr/bin/python3
"""State module - defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class - represents a state

    Attributes:
        name (str): State name
    """

    name = ""
