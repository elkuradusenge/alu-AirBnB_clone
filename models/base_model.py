#!/usr/bin/python3
"""BaseModel module - parent class for all models"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class - defines common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance

        Args:
            *args: Variable length argument list (unused)
            **kwargs: Arbitrary keyword arguments for recreation from dict
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance

        Returns:
            dict: Dictionary containing all instance attributes plus __class__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
