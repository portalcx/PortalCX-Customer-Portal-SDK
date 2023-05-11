#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
base_model.py
-------------
This module defines the BaseModel class, which provides a reusable method
for converting a model object to a dictionary.
"""

from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    """
    BaseModel class that extends Pydantic's BaseModel
    """

    class Config:
        """
        Pydantic's model configuration class
        """
        orm_mode = True

    def to_dict(self) -> dict:
        """
        Convert the model object to a dictionary.

        :return: A dictionary representation of the model object
        
        Note that dict(exclude_unset=True) will exclude attributes
        that are not set from the resulting dictionary, if you want
        all attributes to be present with None values for those not
        set, you can simply use self.dict().
        """
        return self.dict(exclude_unset=False)
