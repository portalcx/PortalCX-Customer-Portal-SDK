#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: customer_portal_create_request.py

Description:
This module defines the Stage and CustomerPortalCreateRequest classes used to represent
the data required for creating a new portal in the PortalCX API.
"""

from typing import List, Optional
from .base_model import BaseModel


class Stage:
    def __init__(self, name: str, label: str, description: str, order: int):
        """
        Initialize the Stage object.

        :param name: The name of the stage
        :param label: The label for the stage
        :param description: A description for the stage
        :param order: The order of the stage in the list
        """
        self.name = name
        self.label = label
        self.description = description
        self.order = order


class CustomerPortalCreateRequest(BaseModel):
    def __init__(self, customerEmail: str, customerName: str, customerPhone: str, projectName: str,
                 stages: List[Stage], address1: Optional[str] = None, city: Optional[str] = None,
                 stateCode: Optional[str] = None, zip: Optional[str] = None, address2: Optional[str] = None,
                 projectContactEmail: Optional[str] = None, projectContactPhone: Optional[str] = None,
                 enableReferrals: Optional[bool] = False):
        """
        Initialize the CustomerPortalCreateRequest object.

        :param customerEmail: The email of the customer
        :param customerName: The name of the customer
        :param customerPhone: The phone number of the customer
        :param projectName: The name of the project
        :param stages: A list of Stage objects
        :param address1: The first line of the address (optional)
        :param city: The city (optional)
        :param stateCode: The state code (optional)
        :param zip: The ZIP code (optional)
        :param address2: The second line of the address (optional)
        :param projectContactEmail: The email of the project contact (optional)
        :param projectContactPhone: The phone number of the project contact (optional)
        :param enableReferrals: A flag to enable referrals (optional, default is False)
        """
        self.customerEmail = customerEmail
        self.customerName = customerName
        self.customerPhone = customerPhone
        self.projectName = projectName
        self.stages = stages
        self.address1 = address1
        self.city = city
        self.stateCode = stateCode
        self.zip = zip
        self.address2 = address2
        self.projectContactEmail = projectContactEmail
        self.projectContactPhone = projectContactPhone
        self.enableReferrals = enableReferrals
