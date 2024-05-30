#!/usr/bin/python3
"""BaseModel from which other class is derived"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
            initialize attributes for new objects

            Args:
                *args (any): Unused.
                **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    continue
                if key in ("updated_at", "created_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
            String representation of an Object
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates time of last object update
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an object
        """
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
