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

from portalcx.api.admin_template import CreateTemplate, TemplateStageCreateRequest
from portalcx.utils.logger import logging
from tests.base_test import BaseTest
from tests.base_test import AssertResponse


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
            title="Fun Internet Links",
            contactEmail="projectmanager@solarcompany.com",
            contactPhone="1234567899",
            companyName="Just Another Company",
            color=None,
            templateAppLogoUpload=None,
            emailLogoUpload=None,
            isCustomerReferrals=True,
            isLogoUpdate=None,
            isEmailLogoUpdate=None,
            countryId=1
        )


        response_data = self.pxc.create_template(template_data=template_data)

        AssertResponse.assert_status_code(response_data, 200)
        # AssertResponse.assert_message(response_data, "some string")
        AssertResponse.assert_data(response_data, None) 
        template_id = response_data['message'].replace('"', '')
        assert isinstance(template_id, str)
        assert re.match(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", template_id) is not None

        return template_id

    @pytest.mark.dependency(depends=["test_create_template"])
    def test_create_template_stages(self, template_id):
        """
        Creates three template stages and returns their IDs.
        """
        
        def assert_data_stage_response(response_data: dict):
            data = response_data['data']
            assert isinstance(data, dict), "data is not a dictionary"
            assert 'name' in data, "name key is not in data"
            assert isinstance(data['name'], str), "name is not a string"
            assert 'description' in data, "description key is not in data"
            assert isinstance(data['description'], str), "description is not a string"
            assert 'button_copy' in data, "button_copy key is not in data"
            assert isinstance(data['button_copy'], str), "button_copy is not a string"
            assert 'button_url' in data, "button_url key is not in data"
            assert isinstance(data['button_url'], str), "button_url is not a string"
            assert re.match(r"https?://\S+", data['button_url']), "button_url is not a valid URL"

        # Get the templateId from the previous test
        template_id = self.test_create_template()

        stage_data = [
            {
                "name": "Stage 1 - A Soft Murmur",
                "description": "This website allows you to customize ambient sounds (rain, thunder, waves, etc.) to create your own peaceful soundscape. It's great for focusing, meditating, or simply relaxing.",
                "button_copy": "A Soft Murmur",
                "button_url": "https://asoftmurmur.com/"
            },
            {
                "name": "Stage 2 - The Useless Web",
                "description": "A fun website that takes you to random, entertaining, and 'useless' websites around the internet.",
                "button_copy": "The Useless Web",
                "button_url": "https://theuselessweb.com/"
            },
            {
                "name": "Stage 3 - Window Swap",
                "description": "On this site, people from around the world submit videos of the view from their windows. It's a fascinating way to see different parts of the world from the comfort of your own home.",
                "button_copy": "Window Swap",
                "button_url": "https://window-swap.com/"
            }
        ]

        for data in stage_data:
            stage_request = TemplateStageCreateRequest(
                templateStageId=None,
                templateId=template_id,
                stageName=data["name"],
                stageDescription=data["description"],
                stagePromptButtonCopy=data["button_copy"],
                stagePromptButtonUrl=data["button_url"]
            )

            response_data = self.pxc.create_template_stage(stage_data=stage_request)
            
            AssertResponse.assert_status_code(response_data, 200)
            AssertResponse.assert_message(response_data, "Template Stage created successfully")
            AssertResponse.assert_data(response_data, None)

            if isinstance(response_data['data'], dict):
                assert_data_stage_response(response_data)

    def test_project_and_stages_flow(self):
        """
        Test the flow of creating a project, creating stages,
        creating a customer, deleting stages, and deleting the project.
        """

        # 1. Create New Project Template
        template_id = self.test_create_template()
        logging.info('TEST STARTED: Creating project. Project created with ID: {template_id}')

        # 2. Create 3 New Stages For New Project Template
        self.test_create_template_stages(template_id)
        logging.info('TEST STARTED: Creating stages for the project. Stages created for project ID: {template_id}')

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

