#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel



class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}
