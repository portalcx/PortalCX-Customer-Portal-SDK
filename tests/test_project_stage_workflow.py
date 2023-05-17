#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_project_stage_workflow.py
------------------------------------
Unit tests for the workflow involving project and stage creation/deletion in the PortalCX API class.
"""

import datetime
import json
import re
import time
from json import JSONEncoder

import pytest

from portalcx.api.admin_template import CreateTemplate
from portalcx.utils.logger import logging
from tests.base_test import BaseTest


class PortalStageChangeRequestEncoder(JSONEncoder):
    """
    Custom JSON encoder for serializing objects to JSON with specific handling for datetime objects.
    """

    def default(self, obj: object) -> object:
        """
        Override the default method to customize serialization for specific object types.

        Args:
            obj: The object to be serialized.

        Returns:
            Serialized JSON representation of the object.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class TestTemplateAndProjectFlow(BaseTest):
    
    def extract_stage_ids(self, response_data: dict) -> dict:
        """
        Extracts stage ids from the API response data.

        :param response_data: The JSON response data from the API
        :return: A dictionary mapping stage names to their ids
        """
        stage_ids = {}

        # Check if the required keys exist in the response data
        if 'data' in response_data and 'projectStages' in response_data['data']:
            for stage in response_data['data']['projectStages']:
                if 'stageName' in stage and 'projectStageId' in stage:
                    # Use the stage name as the key and the stage id as the value
                    stage_ids[stage['stageName']] = stage['projectStageId']

        return stage_ids

    @pytest.mark.dependency()
    def test_create_template(self):
        """
        Creates a template and returns its ID.
        """
        template_data = CreateTemplate(
            templateId=None,
            companyId=None,
            title="Test Project 1",
            contactEmail="projectmanager@solarcompany.com",
            contactPhone="1234567899",
            companyName="Solar Company",
            color=None,
            templateAppLogoUpload=None,
            emailLogoUpload=None,
            isCustomerReferrals=True,
            isLogoUpdate=None,
            isEmailLogoUpdate=None,
            countryId=1
        )


        template_id = self.pxc.create_template(template_data=template_data)

        assert template_id is not None
        assert isinstance(template_id, str)
        assert re.match(r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$', template_id) is not None

        return template_id

    # @pytest.mark.dependency(depends=["test_create_project"])
    # ADD CREATE STAGES

    def test_project_and_stages_flow(self):
        """
        Test the flow of creating a project, creating stages,
        creating a customer, deleting stages, and deleting the project.
        """

        # 1. Create a project
        project_id = self.test_create_template()
        logging.info('TEST STARTED: Creating project. Project created with ID: {project_id}')

        # # 2. Create 3 stages for the project
        # self.create_stages(project_id)
        # logging.info('TEST STARTED: Creating stages for the project. Stages created for project ID: {project_id}')

        # # 3. Create a customer for the project
        # portal_id = self.create_customer(project_id)
        # logging.info('TEST STARTED: Creating customer for the project. Customer created for project ID: {project_id} with portal ID: {portal_id}')

        # # 4. Update stages to completed with 10 seconds pause in between
        # self.complete_all_stages(portal_id, project_id)
        # logging.info('TEST STARTED: Updating stages to completed. Stages updated to completed for project ID: {project_id}')

        # 5. Delete each stage from the project.
        # self.delete_stages(project_id)
        # logging.info('TEST STARTED: Deleting stages from the project. Stages deleted from project ID: {project_id}')

        # 6. Delete the project
        # self.delete_project(project_id)
        # logging.info('TEST STARTED: Deleting the project. Project deleted with ID: {project_id}')

