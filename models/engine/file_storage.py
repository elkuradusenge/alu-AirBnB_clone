#!/usr/bin/python3
"""FileStorage module - handles JSON serialization/deserialization"""
import json


class FileStorage:
    """FileStorage class - serializes/deserializes instances to/from JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id

        Args:
            obj: Object instance to store
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects if file exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value['__class__']
                if class_name in classes:
                    cls = classes[class_name]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
