#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name:
api/api_base.py

description:
Base class for API integration in the Azure Python Function App.
"""

import httpx
from abc import ABC, abstractmethod
from utils.logger import get_logger


class APIBaseError(Exception):
    """
    Custom exception class for APIBase errors.
    """

    def __init__(self, status_code, error_message):
        """
        Initialize the APIBaseError exception.

        :param status_code: The status code from the API response
        :param error_message: The error message from the API response
        """
        self.status_code = status_code
        self.error_message = error_message
        super().__init__(f"API Error (Code: {status_code}): {error_message}")


class APIBase(ABC):
    """
    Base class for API integration.
    """

    def __init__(self, base_url, auth_token=None):
        """
        Initialize the API base class with base URL and optional authentication token.

        :param base_url: The base URL of the API
        :param auth_token: The authentication token (optional)
        """
        self.base_url = base_url
        self.auth_token = auth_token
        self.logger = get_logger()
    
    def process_response(self, response: httpx.Response) -> dict:
        """
        Process an HTTP response.

        :param response: The HTTP response
        :return: The JSON response data
        :raise: APIBaseError if the request fails
        """
        response_data = response.json()

        if response.status_code != 200:
            self.logger.error(f"API request failed: {response_data.get('errorMessage', 'Unknown error')}")
            raise APIBaseError(response.status_code, response_data.get('errorMessage', 'Unknown error'))

        return response_data

    def request(self, method, endpoint, **kwargs):
        """
        Make an HTTP request to the specified API endpoint.

        :param method: The HTTP method to use (e.g., 'GET', 'POST', etc.)
        :param endpoint: The API endpoint to call
        :param kwargs: Additional arguments to pass to the httpx.request method
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
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

            # Check if response object is available and raise APIBaseError with status code and error message
            if hasattr(status_error, 'response') and status_error.response is not None:
                error_message = status_error.response.json().get('errorMessage', 'Unknown error')
                raise APIBaseError(status_error.response.status_code, error_message)

            else:
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
