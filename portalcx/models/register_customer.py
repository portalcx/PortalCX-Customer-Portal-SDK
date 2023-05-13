#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/customer_data.py
----------------------
This file contains code for representing customer data.
"""

from __future__ import annotations

from .base_model import BaseModel

class CustomerData(BaseModel):
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

    def __repr__(self) -> str:
        return (
            f"CustomerData(email='{self.email}', password='{self.password}', phone='{self.phone}', "
            f"companyName='{self.companyName}', contactPhone='{self.contactPhone}', "
            f"firstName='{self.firstName}', lastName='{self.lastName}')"
        )

    def __str__(self) -> str:
        return (
            f"CustomerData({self.email}, {self.phone}, {self.companyName}, "
            f"{self.contactPhone}, {self.firstName}, {self.lastName})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CustomerData):
            return NotImplemented
        return (
                self.email == other.email
                and self.phone == other.phone
                and self.companyName == other.companyName
                and self.contactPhone == other.contactPhone
                and self.firstName == other.firstName
                and self.lastName == other.lastName
        )
