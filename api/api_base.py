#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name:
shared_code/api/api_base.py

description:
Base class for API integration in the Azure Python Function App.
"""


import httpx
from abc import ABC, abstractmethod
from shared_code.utils.logger import Logger

class APIBase(ABC):
    def __init__(self, base_url, auth_token=None):
        """
        Initialize the API base class with base URL and optional authentication token.

        :param base_url: The base URL of the API
        :param auth_token: The authentication token (optional)
        """
        self.base_url = base_url
        self.auth_token = auth_token
        self.logger = Logger(__name__)

    def request(self, method, endpoint, **kwargs):
        """
        Make an HTTP request to the specified API endpoint.

        :param method: The HTTP method to use (e.g., 'GET', 'POST', etc.)
        :param endpoint: The API endpoint to call
        :param kwargs: Additional arguments to pass to the httpx.request method
        :return: The JSON response from the API
        :raise: Exception if the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = kwargs.pop('headers', {})
        
        # Add the authentication token to headers if it exists
        if self.auth_token:
            headers['Authorization'] = f"Bearer {self.auth_token}"
        
        # Use httpx to make the request
        try:
            response = httpx.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
        except httpx.HTTPStatusError as status_error:
            self.logger.error(f"API request failed with status error: {status_error}")
            raise
        except httpx.RequestError as request_error:
            self.logger.error(f"API request failed with request error: {request_error}")
            raise
        except Exception as e:
            self.logger.error(f"API request failed: {e}")
            raise

        # Process the JSON response
        try:
            return response.json()
        except ValueError:
            self.logger.error("API response could not be parsed as JSON")
            raise
