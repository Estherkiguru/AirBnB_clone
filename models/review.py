#!/usr/bin/python3
"""module for class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherited Review class
    """
    place_id = ""
    user_id = ""
    text = ""
