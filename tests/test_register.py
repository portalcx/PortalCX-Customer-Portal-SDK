#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_portalcx.py
----------------------
Unit tests for the PortalCX API class.
"""
import pytest
from tests.base_test import BaseTest
from portalcx.models.auth_management_models import AuthManagementRegister


class TestAuthManagementRegister(BaseTest):

    @pytest.mark.skip(reason="Already Registered")
    def test_register(self):
        """
        Test the register function of the PortalCX API class.
        """

        # Prepare sample registration data
        user_data = AuthManagementRegister(
            email="test@portalcx.com",
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
