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
            email="thedude@portalcx.com",
            password="TheDudePassword",
            firstName="The",
            lastName="Dude",
            phone="8011234456",
            companyName="The Dudes Company Name",
            contactPhone="8011234456"
        )

        response_data = self.pxc.register(user_data=user_data)

        self.register_data_validation(response_data)

    def register_data_validation(self, response_data):
        """
        Validate Data Returned From The Register API
        
        Example Data:
        
        response_data = {
            'status': 200, 
            'message': '', 
            'data': {
                'userCompanyInfo': None, 
                'companyId': 99, 
                'result': True, 
                'errors': None, 
                'token': 'Some_Long_Token', 
                'stripeCustomerId': 'cus_StripeCustomerId'
            }
        }
        """

        assert isinstance(response_data, dict), "Data should be a dictionary"
        assert isinstance(response_data['status'], int), "Status should be an integer"
        assert response_data['status'] == 200, "Status should be 200"
        assert isinstance(response_data['message'], str), "Message should be a string"
        assert isinstance(response_data['data'], dict), "Data within data should be a dictionary"
        assert isinstance(response_data['data']['companyId'], int), "companyId should be an integer"
        assert isinstance(response_data['data']['result'], bool), "result should be a boolean"
        assert response_data['data']['result'] is True, "result should be True"
        assert response_data['data']['errors'] is None, "errors should be None"
        assert isinstance(response_data['data']['token'], str), "token should be a string"
        assert isinstance(response_data['data']['stripeCustomerId'], str), "stripeCustomerId should be a string"
