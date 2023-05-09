#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name:
tests/test_portalcx.py

description:
Unit tests for the PortalCX API class.
"""

import os
import unittest
import pytest

from portalcx.api.portalcx import PortalCX
from portalcx.models.customer_portal_create_request import CustomerPortalCreateRequest
from portalcx.models.user_registration import UserRegistration


class TestPortalCX(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level variables for the test cases.
        """
        cls.api_base_url = os.environ.get("PORTALCX_API_BASE_URL")
        cls.email = os.environ.get("PORTALCX_EMAIL")
        cls.password = os.environ.get("PORTALCX_PASSWORD")

    @pytest.mark.skip(reason="Already Registered")
    def test_register(self):
        """
        Test the register function of the PortalCX API class.
        """
        portal_cx = PortalCX(api_base_url=self.api_base_url)

        # Prepare sample registration data
        user_data = UserRegistration(
            email="dude@portalcx.com",
            password="somepassword",
            firstName="Dude",
            lastName="Test",
            phone="1234567899",
            companyName="PortalCX Test",
            contactPhone="1234567899"
        )

        response_data = portal_cx.register(user_data=user_data)

        self.assertIsNotNone(response_data)
        self.assertIsInstance(response_data, dict)
        self.assertTrue(response_data.get('result'))

    def test_login(self):
        """
        Test the login function of the PortalCX API class.
        """
        portal_cx = PortalCX(api_base_url=self.api_base_url)
        auth_token = portal_cx.login(email=self.email, password=self.password)
        self.assertIsNotNone(auth_token)
        self.assertIsInstance(auth_token, str)

    def test_create_portal(self):
        """
        Test the create_portal function of the PortalCX API class.
        """
        portal_cx = PortalCX(api_base_url=self.api_base_url)
        auth_token = portal_cx.login(email=self.email, password=self.password)
        self.assertIsNotNone(auth_token)

        # Prepare sample data
        portal_data = CustomerPortalCreateRequest(
            customerEmail="dude@portalcx.com",
            customerName="John Doe",
            customerPhone="1234567899",
            projectName="Home",
            stages=[
                {
                    "name": "Stage 1",
                    "label": "Stage 1 Label",
                    "description": "This is a test stage",
                    "order": 1
                },
                {
                    "name": "Stage 2",
                    "label": "Stage 2 Label",
                    "description": "This is another test stage",
                    "order": 2
                },
                {
                    "name": "Stage 3",
                    "label": "Stage 3 Label",
                    "description": "This is the third test stage",
                    "order": 3
                }
            ],
            address1="123 Test Street",
            city="Test City",
            stateCode="TS",
            zip="12345",
            enableReferrals=True
        )

        response_data = portal_cx.create_portal(portal_data=portal_data)

        self.assertIsNotNone(response_data)
        self.assertIsInstance(response_data, dict)
        if "portalId" in response_data:
            portalId = response_data["portalId"]
            self.assertIsNotNone(portalId)
            self.assertIsInstance(portalId, str)
            self.assertRegex(portalId, r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$')


if __name__ == "__main__":
    unittest.main()
