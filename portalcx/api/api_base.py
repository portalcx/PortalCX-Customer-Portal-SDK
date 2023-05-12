#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/api_base.py
---------------
Base class for API integration in the Azure Python Function App.
"""

from abc import ABC
from json import JSONDecodeError
import json

import httpx

from ..utils.logger import get_logger


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
        if response.status_code not in [200, 204]:  # add other success status codes if needed
            self.handle_error_response(response)

        return self.parse_response_data(response)

    def handle_error_response(self, response: httpx.Response):
        """
        Handle error HTTP response.

        :param response: The HTTP response
        :raise: APIBaseError
        """
        response_data = self.parse_response_data(response)
        self.logger.error(f"API request failed: {response_data.get('errorMessage', 'Unknown error')}")
        raise APIBaseError(response.status_code, response_data.get('errorMessage', 'Unknown error'))

    def parse_response_data(self, response: httpx.Response) -> dict:
        """
        Parse HTTP response data.

        :param response: The HTTP response
        :return: The parsed response data
        """
        try:
            # temporary until we return only JSON from api.portalcx.com
            if 'deleted' in response.text:
                return_response = response.text
            else:
                return_response = response.json()
        except (JSONDecodeError, json.JSONDecodeError):
            if response.text:
                return_response = response.text
            else:
                return_response = {}

        return return_response

    def request(self, method, endpoint, **kwargs):
        """
        Make an HTTP request to the specified API endpoint.

        :param method: The HTTP method to use (e.g., 'GET', 'POST', etc.)
        :param endpoint: The API endpoint to call
        :param kwargs: Additional arguments to pass to the httpx.request method
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop('headers', {})

        # Add the authentication token to headers if it exists
        if self.auth_token:
            headers['Authorization'] = f"Bearer {self.auth_token}"

        # Use httpx to make the request
        try:
            response = httpx.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
        except httpx.HTTPStatusError as status_error:
            self.handle_http_status_error(status_error)
        except httpx.RequestError as request_error:
            self.handle_request_error(request_error)
        except Exception as e:
            self.handle_generic_error(e)

        # Process the JSON response using process_response method
        return self.process_response(response)

    def handle_http_status_error(self, status_error: httpx.HTTPStatusError):
        """
        Handle httpx HTTP status errors.

        :param status_error: The httpx HTTPStatusError
        :raise: APIBaseError
        """
        self.logger.error(f"API request failed with status error: {status_error}")

        # Check if response object is available and raise APIBaseError with status code and error message
        if hasattr(status_error, 'response') and status_error.response is not None:
            error_message = self.get_error_message_from_response(status_error.response)

            # Log the entire response content for better debugging
            self.logger.error(f"Error response from the API: {status_error.response.content}")

            # Use the logger to log the error message before raising the error
            self.logger.error(f"Error message from the API: {error_message}")

            raise APIBaseError(status_error.response.status_code, error_message)
        else:
            raise

    def handle_request_error(self, request_error: httpx.RequestError):
        """
        Handle httpx request errors.

        :param request_error: The httpx RequestError
        :raise: request_error
        """
        self.logger.error(f"API request failed with request error: {request_error}")
        raise

    def handle_generic_error(self, e: Exception):
        """
        Handle generic errors.

        :param e: The error
        :raise: e
        """
        self.logger.error(f"API request failed: {e}")
        raise

    def get_error_message_from_response(self, response: httpx.Response) -> str:
        """
        Extract error message from httpx response.

        :param response: The httpx response
        :return: The error message
        """
        try:
            error_message = response.json().get('errorMessage', 'Unknown error')
        except JSONDecodeError:
            error_message = response.text

        return error_message
