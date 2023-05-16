#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/auth_management.py
----------------------
This module represents all API calls in the /api/AuthManagement section.
"""

from typing import Dict

from ..models.auth_management_models import AuthManagementRegister, UserLoginRequest
from .api_base import APIBase


class AuthManagement(APIBase):
    """
    Class for managing authentication-related operations.
    """

    def __init__(self, base_url: str):
        super().__init__(base_url)

    def register(self, user_data: AuthManagementRegister) -> Dict:
        """
        Registers a new user with the provided information.

        :param user_data: A UserRegistration object containing the user information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        register_url = "/api/AuthManagement/Register"
        self.logger.info(f"Registering a new user with email: {user_data.email}")
        
        # Make the request and process the response
        response_data = self.request("POST", register_url, json=user_data.to_dict())
        
        self.logger.info("Successfully registered a new user")

        return response_data

    def login(self, email: str, password: str) -> str:
        """
        Logs into the PortalCX API with the provided credentials.

        :param email: The email of the user
        :param password: The password of the user
        :return: The token received from the login operation
        """
        login_url = "/api/AuthManagement/Login"
        user_login_request = UserLoginRequest(email=email, password=password)

        # Log the attempt
        self.logger.info(f"Logging into PortalCX API with email: {user_login_request.email}")

        # Make the request and process the response
        response_data = self.request("POST", login_url, json=user_login_request.to_dict())

        # Save the token
        self.token = response_data.get("token")

        self.logger.info("Successfully logged into PortalCX API")

        return self.token
