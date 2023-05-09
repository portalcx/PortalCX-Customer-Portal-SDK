#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name:
api/portalcx.py

description:
Class representing the PortalCX API.
"""

from typing import Dict

from .api_base import APIBase, APIBaseError
from ..models.customer_portal_create_request import CustomerPortalCreateRequest
from ..models.user_registration import UserRegistration

from utils.logger import get_logger


class PortalCX(APIBase):
    """
    Class representing the PortalCX API.
    """

    def __init__(self, api_base_url: str):
        super().__init__(api_base_url)
        self.logger = get_logger()
    
    def register(self, user_data: UserRegistration) -> dict:
        """
        Registers a new user with the provided information.

        :param user_data: A UserRegistration object containing the user information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        register_url = "/api/AuthManagement/Register"
        self.logger.info(f"Registering a new user with email: {user_data.email}")
        response_data = self.request("POST", register_url, json=user_data.to_dict())
        self.logger.info("Successfully registered a new user")

        return response_data

    def login(self, email: str, password: str) -> str:
        """
        Logs into the PortalCX API with the provided credentials.
        """
        login_url = "/api/AuthManagement/Login"
        body = {"email": email, "password": password}
        self.logger.info(f"Logging into PortalCX API with email: {email}")
        response_data = self.request("POST", login_url, json=body)
        self.auth_token = response_data.get("token")
        self.logger.info("Successfully logged into PortalCX API")

        return self.auth_token
    
    def create_portal(self, portal_data: CustomerPortalCreateRequest) -> dict:
        """
        Creates a new portal with the provided data.

        :param portal_data: A CustomerPortalCreateRequest object containing the portal data
        :return: The JSON response from the API
        :raise: PortalCXError if the request fails
        """
        create_portal_url = "/api/Customer/portal/create"
        self.logger.info("Creating a new portal")
        self.logger.info(f"Using the following data to Create Portal: {portal_data.to_dict()}")
        response_data = self.request("POST", create_portal_url, json=portal_data.to_dict())
        self.logger.info("Successfully created a new portal")

        return response_data

