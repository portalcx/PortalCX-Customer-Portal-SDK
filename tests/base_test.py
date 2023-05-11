#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/base_test.py
------------------
Base test class for PortalCX tests.
"""

import os

import pytest

from portalcx.api.portalcx import PortalCX


class BaseTest:

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, request):
        """
        Set up class-level variables for the test cases.
        """
        self.api_base_url = os.environ.get("PORTALCX_API_BASE_URL")
        self.email = os.environ.get("PORTALCX_EMAIL")
        self.password = os.environ.get("PORTALCX_PASSWORD")

        self.portal_cx = PortalCX(api_base_url=self.api_base_url)
        request.cls.portal_cx = self.portal_cx

        auth_token = self.portal_cx.login(email=self.email, password=self.password)
        assert auth_token is not None
        assert isinstance(auth_token, str)

        self.portal_cx.token = auth_token
        request.cls.token = auth_token
