#!/usr/bin/env python3
'''Defines a class FileStorage'''
import json
import os
import sys
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''Serializes instances to a JSON file and also deserializes
    JSON file to instances
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary "__objects"'''

        return self.__objects

    def new(self, obj):
        '''Sets in "__objects" the obj with the key
        "<obj classname>.id"
        Example: to store a BaseModel object with id=123,
        the key BaseModel.123
        '''

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''Serializes "__objects" to the JSON file'''

        obj_data = {}
        for key, value in self.__objects.items():
            obj_data[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obj_data, f)

    def reload(self):
        '''Deserializes the JSON file to "__objects"'''

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]  #: Get class by name
                    obj = cls(**value)  #: Instantiate the object
                    self.__objects[key] = obj  #: Store object
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
