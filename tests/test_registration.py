#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_portalcx.py
----------------------
Unit tests for the PortalCX API class.
"""
import pytest

from portalcx.api.portalcx import PortalCX
from portalcx.models.user_registration import UserRegistration
from tests.base_test import BaseTest


class TestPortalCX(BaseTest):

    @pytest.mark.skip(reason="Already Registered")
    def test_register(self):
        """
        Test the register function of the PortalCX API class.
        """
        portal_cx = PortalCX(api_base_url=self.api_base_url)

        # Prepare sample registration data
        user_data = UserRegistration(
            email="dude@portalcx.com",
            password="SomeRandomPassword",
            firstName="The",
            lastName="Dude",
            phone="1234567899",
            companyName="The Dudes Company",
            contactPhone="9876543211"
        )

        response_data = portal_cx.register(user_data=user_data)

        assert response_data is not None
        assert isinstance(response_data, dict)
        assert response_data.get('result')
