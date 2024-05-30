#!/usr/bin/python3
"""
    Handles JSON serialization-deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Represents a storage medium

    Attributes:
        __file_path(str): serves as input point
        __objects (dict): A dictionary object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """adds object by key to __object dictionary """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
            serializes __objets to JSON file.
        """
        with open(self.__file_path, 'w') as fp:
            json.dump({key: value.to_dict() for key, value
                       in self.__objects.items()}, fp)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as fp:
                objects = json.load(fp)
                for key, value in objects.items():
                    if value['__class__'] == 'User':
                        self.__objects[key] = User(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
