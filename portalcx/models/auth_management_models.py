#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
auth_management.py
------------------
This file contains code for representing authorization and authentication data.
"""

from __future__ import annotations

from .base_model import BaseModel

class AuthManagementRegister(BaseModel):
    """
    This class represents customer data.
    """
    email: str
    password: str
    contactPhone: str
    companyName: str
    phone: str
    firstName: str
    lastName: str


class UserLoginRequest(BaseModel):
    """
    This class represents a user login request.
    """
    email: str
    password: str
