#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
base_model.py
-------------
This module defines the BaseModel class, which provides a reusable method
for converting a model object to a dictionary.
"""

from typing import Any, Dict
from pydantic import BaseModel as PydanticBaseModel


def to_camel(string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Args:
        string (str): The string in snake_case to convert.

    Returns:
        str: The converted string in camelCase.
    """
    components = string.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


class BaseModel(PydanticBaseModel):
    """
    BaseModel class that extends Pydantic's BaseModel
    """

    class Config:
        """
        Pydantic's model configuration class. This is used to control the behavior
        of the BaseModel. For example, it can be used to set case styles for variable names,
        to enable or disable ORM mode, or to control how fields are populated.
        """
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True
        allow_population_by_alias = True

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the model object to a dictionary.

        :return: A dictionary representation of the model object
        """
        return self.dict(exclude_unset=True, exclude_none=True)
