#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
user_registration.py
--------------------
This module defines the UserRegistration class used to represent
the data required for registering a new user in the PortalCX API.
"""

from typing import Optional
from .base_model import BaseModel


class UserRegistration(BaseModel):
    def __init__(self, email: str, password: str, firstName: str, lastName: str,
                 companyName: str, contactPhone: str, phone: Optional[str] = None):
        """
        Initialize the UserRegistration object.

        :param email: The email address of the user
        :param password: The password for the user
        :param firstName: The first name of the user
        :param lastName: The last name of the user
        :param phone: The phone number of the user (optional)
        :param companyName: The name of the company creating a new account
        :param contactPhone: The phone number of the company creating a new account

        """
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.companyName = companyName
        self.contactPhone = contactPhone
