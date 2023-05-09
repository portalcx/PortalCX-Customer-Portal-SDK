#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: base_model.py

Description:
This module defines the BaseModel class, which provides a reusable method
for converting a model object to a dictionary.
"""

class BaseModel:
    def to_dict(self) -> dict:
        """
        Convert the model object to a dictionary.

        :return: A dictionary representation of the model object
        """
        return {key: value for key, value in self.__dict__.items() if value is not None}
