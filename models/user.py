#!/usr/bin/python3
"""Defines User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from the BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
