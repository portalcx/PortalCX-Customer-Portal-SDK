#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
portal_customer_models.py
-------------------------
Models for customer related operations.
"""

from typing import Optional
from .base_model import BaseModel


class PortalCustomerCreateRequest(BaseModel):
    """
    Represents a request to create a new customer.
    """
    portalCustomerId: Optional[int] = None
    projectId: str
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    address: Optional[str] = None
    city: Optional[str] = None
    stateCode: Optional[str] = None
    zip: Optional[str] = None
    notifyViaEmail: bool
    notifyViaSMS: bool
    completeFirstStage: bool
    countryId: int
