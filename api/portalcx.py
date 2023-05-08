#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name:
api/portalcx.py

description:
Class representing the PortalCX API.
"""

from typing import Dict
from api.api_base import APIBase, APIBaseError
from models.customer_portal import CustomerPortal
from utils.logger import get_logger


class PortalCXError(APIBaseError):
    pass  # Inheriting from APIBaseError


class PortalCXError(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message
        super().__init__(f"PortalCX API Error (Code: {status_code}): {error_message}")


class PortalCX(APIBase):
    """
    Class representing the PortalCX API.
    """

    def __init__(self, api_base_url: str):
        super().__init__(api_base_url)
        self.logger = get_logger()

    def login(self, email: str, password: str) -> str:
        """
        Logs into the PortalCX API with the provided credentials.
        """
        login_url = "AuthManagement/Login"
        body = {"email": email, "password": password}
        self.logger.info(f"Logging into PortalCX API with email: {email}")
        response_data = self.request("POST", login_url, json=body)
        self.auth_token = response_data.get("token")
        self.logger.info("Successfully logged into PortalCX API")

        return self.auth_token
