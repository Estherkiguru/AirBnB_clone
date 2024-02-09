#!/usr/bin/env python3
'''Defines the class BaseModel'''
from datetime import datetime
import json
import uuid


class BaseModel:
    '''Definition of a base class from which other classes will inherit
    '''

    def __init__(self, *args, **kwargs):
        '''Initialises a new object

        args (any): arguments passed for the constructor
        kwargs (dict): keyword arguments
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key in ["created_at", "updated_at"]:
                        setattr(self,
                                key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def save(self):
        '''Update the attribute 'updated_at' with the current
        date and time
        '''

        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all key/values
        of '__dict__' of the instance
        '''

        obj_dict = dict()
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                obj_dict[key] = self.__dict__[key].strftime(
                        "%Y-%m-%dT%H:%M:%S.%f")
            else:
                obj_dict[key] = value

        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict

    def __str__(self):
        '''Returns the informal string representation of an object
        '''

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
