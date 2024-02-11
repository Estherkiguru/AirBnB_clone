#!/usr/bin/python3
"""module for class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherited city class
    contains name and state_id attributes
    """
    state_id = ""
    name = ""
