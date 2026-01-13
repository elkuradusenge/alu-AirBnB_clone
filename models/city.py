#!/usr/bin/python3
"""City module - defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class - represents a city

    Attributes:
        state_id (str): State ID
        name (str): City name
    """

    state_id = ""
    name = ""
