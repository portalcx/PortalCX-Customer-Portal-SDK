#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: CreateCustomerPortal/__init__.py

Description:

Azure Function for creating a customer portal in PortalCX.
"""

import logging
import httpx
from typing import Dict
from shared_code.api.api_base import APIBase

class PortalCX(APIBase):
    """
    Class representing the PortalCX API.
    """

    def __init__(self, api_base_url: str):
        super().__init__(api_base_url)
    
    def login(self, email: str, password: str) -> Dict:
        """
        Logs into the PortalCX API with the provided credentials.

        Parameters:
        email (str): Email address for the user account.
        password (str): Password for the user account.

        Returns:
        response_data (dict): Response data from the API, including the auth token.
        """
        login_url = self.base_url + "AuthManagement/Login"
        headers = {"Content-Type": "application/json"}
        body = {"email": email, "password": password}

        with httpx.Client() as client:
            response = client.post(login_url, json=body, headers=headers)

        response_data = response.json()

        if response.status_code != 200:
            logging.error(f"PortalCX login failed: {response_data.get('errorMessage', 'Unknown error')}")
            raise Exception(f"PortalCX login failed: {response_data.get('errorMessage', 'Unknown error')}")

        return response_data
    
    def create_customer_portal(self, data: Dict) -> Dict:
        """
        Creates a new customer portal in PortalCX with the provided data.

        Parameters:
        data (dict): Data for creating the customer portal.

        Returns:
        response_data (dict): Response data from the API, including the portal ID.
        """
        create_portal_url = self.base_url + "Customer/portal/create"
        headers = {"Authorization": f"Bearer {self.auth_token}", "Content-Type": "application/json"}

        with httpx.Client() as client:
            response = client.post(create_portal_url, json=data, headers=headers)

        response_data = response.json()

        if response.status_code != 200:
            logging.error(f"PortalCX customer portal creation failed: {response_data.get('errorMessage', 'Unknown error')}")
            raise Exception(f"PortalCX customer portal creation failed: {response_data.get('errorMessage', 'Unknown error')}")

        return response_data
