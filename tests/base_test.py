#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/base_test.py
------------------
Base test class for PortalCX tests.
"""

import os

import pytest

from portalcx import PortalCX


class BaseTest:

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, request):
        """
        Set up class-level variables for the test cases.
        """
        self.api_base_url = os.environ.get("PORTALCX_API_BASE_URL")
        self.email = os.environ.get("PORTALCX_EMAIL")
        self.password = os.environ.get("PORTALCX_PASSWORD")

        self.pxc = PortalCX(base_url=self.api_base_url)
        request.cls.pxc = self.pxc

        auth_token = self.pxc.login(email=self.email, password=self.password)
        assert auth_token is not None
        assert isinstance(auth_token, str)

        self.pxc.token = auth_token
        request.cls.token = auth_token

class AssertResponse:

    @staticmethod
    def assert_status_code(response_data, expected_status):
        assert response_data['status'] == expected_status, f"Expected status code {expected_status}, got {response_data['status']}"

    @staticmethod
    def assert_message(response_data, expected_message):
        assert response_data['message'] == expected_message, f"Expected message '{expected_message}', got '{response_data['message']}'"

    @staticmethod
    def assert_data(response_data, expected_data):
        assert response_data['data'] == expected_data, f"Expected data '{expected_data}', got '{response_data['data']}'"
