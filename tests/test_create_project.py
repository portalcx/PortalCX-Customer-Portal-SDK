#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_create_project.py
----------------------------
Unit tests for the create_project function of the PortalCX API class.
"""
import re

from portalcx.models.project_models import CreateProjectRequest
from tests.base_test import BaseTest


class TestCreateProject(BaseTest):

    def test_create_project(self):
        """
        Test the create_project function of the PortalCX API class.
        """
        project_data = CreateProjectRequest(
            # ProjectId=None,
            # CompanyId=None,
            Title="Solar Installation",
            ContactEmail="projectmanager@solarcompany.com",
            ContactPhone="1234567890",
            CompanyName="Solar Company",
            # Color=None,
            # PortalAppLogoUpload=None,
            # EmailLogoUpload=None,
            IsCustomerReferrals=True,
            # IsLogoUpdate=None,
            # IsEmailLogoUpdate=None,
            # CountryId=None
        )
        response_data = self.pxc.create_project(project_data=project_data)
        assert response_data is not None
        assert isinstance(response_data, dict)
        if "ProjectId" in response_data:
            projectId = response_data["ProjectId"]
            assert projectId is not None
            assert isinstance(projectId, str)
            assert re.match(r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$', projectId) is not None
