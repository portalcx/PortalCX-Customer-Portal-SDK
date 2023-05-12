#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_portalcx.py
----------------------
Unit tests for the PortalCX API class.
"""
import pytest
from portalcx.models.customer_data_registration import CustomerData
from tests.base_test import BaseTest


class TestPortalCX(BaseTest):

    @pytest.mark.skip(reason="Already Registered")
    def test_register(self):
        """
        Test the register function of the PortalCX API class.
        """

        # Prepare sample registration data
        user_data = CustomerData(
            email="dude@dude.com",
            password="SomePassword",
            firstName="The",
            lastName="Dude",
            phone="1234567899",
            companyName="The Dudes Company",
            contactPhone="9876543211"
        )

        response_data = self.pxc.register(user_data=user_data)

        assert response_data is not None
        assert isinstance(response_data, dict)
        assert response_data.get('result')
