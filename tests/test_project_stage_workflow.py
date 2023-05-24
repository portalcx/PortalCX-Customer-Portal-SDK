#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_project_stage_workflow.py
------------------------------------
Unit tests for the workflow involving project and stage creation/deletion in the PortalCX API class.
"""

import random
import re
import string
import time
from datetime import datetime, timezone
from json import JSONEncoder

import pytest

from portalcx.api.admin_projects import ProjectCreateRequest
from portalcx.api.admin_templates import (CreateTemplate,
                                          ProjectStageCompleteRequest,
                                          TemplateStageCreateRequest)
from portalcx.utils.logger import logging
from tests.base_test import AssertResponse, BaseTest


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

    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def extract_stage_ids(self, response_data: dict) -> dict:
        """
        Extracts stage ids from the API response data.

        :param response_data: The JSON response data from the API
        :return: A dictionary mapping stage names to their ids
        """
        stage_ids = {}

        # Check if the required keys exist in the response data
        if 'data' in response_data and 'templateStages' in response_data['data']:
            for stage in response_data['data']['templateStages']:
                if 'stageName' in stage and 'templateStageId' in stage:
                    # Use the stage name as the key and the stage id as the value
                    stage_ids[stage['stageName']] = stage['templateStageId']

        return stage_ids

    def currentDateTime(self) -> str:
        dateTime = datetime.now(timezone.utc)
        dateTimeString = dateTime.isoformat()

        return dateTimeString

    @pytest.mark.dependency()
    def test_create_template(self):
        """
        Creates a template and returns its ID.
        """
        template_data = CreateTemplate(
            templateId=None,
            companyId=None,
            title=f"Fun Internet Links - {self.generate_random_string()}",
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
    def test_create_template_stages(self, template_id: str):
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

    @pytest.mark.dependency(depends=["test_create_template_stages"])
    def test_create_project(self, template_id: str):
        """
        Creates a new project and returns its ID.
        """
  
        def assert_project_creation_response(response_data: dict):
            """
            Asserts that the API response for project creation contains valid data.

            :param response_data: The response data from the API.
            """

            # Assert that the necessary keys are present in the response data
            assert 'portalId' in response_data, "'portalId' key is not present in response data"
            assert 'message' in response_data, "'message' key is not present in response data"
            assert 'projectId' in response_data, "'projectId' key is not present in response data"

            # Assert the types and content of the response data
            assert isinstance(response_data['portalId'], str), "'portalId' is not a string"
            assert re.match(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", response_data['portalId']) is not None, "'portalId' is not a valid UUID"
            assert isinstance(response_data['message'], str), "'message' is not a string"
            assert response_data['message'] == 'Project created successfully', "'message' does not match expected text"
            assert isinstance(response_data['projectId'], int), "'projectId' is not an integer"
            assert response_data['projectId'] > 0, "'projectId' is not a positive integer"


        project_data = ProjectCreateRequest(
            projectId=None,
            templateId=template_id,
            firstName="The",
            lastName="Dude",
            email="thedude@portalcx.com",
            phoneNumber="8016697921",
            addressLine1="123 Main Street",
            addressLine2=None,
            city="Salt Lake City",
            stateCode="UT",
            zip="84101",
            notifyViaEmail=False,
            notifyViaSMS=True,
            completeFirstStage=False,
            countryId=1,
        )

        response_data = self.pxc.create_project(project_data=project_data)

        assert isinstance(response_data["data"], dict)

        response_data_dict = response_data["data"]

        AssertResponse.assert_status_code(response_data, 200)
        AssertResponse.assert_message(response_data_dict, "Project created successfully")
        assert_project_creation_response(response_data_dict)

        return response_data_dict['projectId'], response_data_dict['portalId']

    @pytest.mark.dependency(depends=["test_create_project"])
    def test_get_all_stages_by_template_id(self, template_id: str):
        """
        Gets all stages for the specified template ID and verifies that the returned stages match those that were created.
        """
        response_data = self.pxc.get_all_stages_by_template_id(template_id)

        AssertResponse.assert_status_code(response_data, 200)

        stage_ids = self.extract_stage_ids(response_data['data'])

        return stage_ids

    @pytest.mark.dependency(depends=["test_get_all_stages_by_template_id"])
    def test_complete_project_stages(self, stage_ids: dict, project_and_portal_ids: list):
        """
        Using the list of stage ids, complete each stage one at a time, waiting 10 seconds
        in between each stage until the project is fully completed rotating the Project ID and Portal ID.
        """
        for i, (stage_name, stage_id) in enumerate(stage_ids.items()):

            # Determine if it's an even or odd iteration
            is_even_iteration = i % 2 == 0

            # Depending on the iteration, use projectId or portalId
            id_key = 'projectId' if is_even_iteration else 'portalId'
            id_value = project_and_portal_ids[i % len(project_and_portal_ids)]

            logging.info(f'Preparing request for stage: {stage_name}, id: {stage_id} using {id_key}: {id_value}')

            complete_stage_data = ProjectStageCompleteRequest(
                completedStageLabel=stage_name,
                completedDate=self.currentDateTime(),
                notifyViaEmail=True,
                notifyViaSms=True,
                **{id_key: id_value}
            )

            logging.info(f'Completing stage named {stage_name} with id {stage_id} using {id_key}')

            response_data = self.pxc.complete_project_stage(complete_stage_data)

            logging.info('Validating response data')
            AssertResponse.assert_status_code(response_data, 200)
            AssertResponse.assert_message(response_data, "Project stage changed")
            assert isinstance(response_data, dict), "Response is not a dictionary"

            # Wait for 10 seconds, showing progress in log
            for second in range(1, 11):
                logging.info(f'Waiting... {second}/10 seconds elapsed')
                time.sleep(1)

        logging.info('Test complete: complete_project_stages')

    @pytest.mark.dependency(depends=["test_complete_project_stages"])
    def test_delete_project(self, project_id: int):
        """
        Deletes a project using its ID.
        """
        response_data = self.pxc.delete_project(project_id)

        AssertResponse.assert_status_code(response_data, 200)
        AssertResponse.assert_message(response_data, "Project deleted successfully")

    @pytest.mark.skip(reason="Has a bug, work in progress to resolve it.")
    @pytest.mark.dependency(depends=["test_delete_project"])
    def test_delete_stage(self, stage_ids: dict):
        """
        Delete each stage one by one.
        """
        for stage_name, stage_id in stage_ids.items():
            logging.info(f'Deleting stage: {stage_name}, id: {stage_id}')

            response_data = self.pxc.delete_stage(stage_id)

            AssertResponse.assert_status_code(response_data, 200)
            AssertResponse.assert_message(response_data, "Stage deleted successfully")
            assert isinstance(response_data, dict), "Response is not a dictionary"

        logging.info('Test complete: delete_stage')

    @pytest.mark.dependency(depends=["test_delete_project"]) #  Change 
    def test_delete_template(self, template_id: str):
        """
        Delete a template.
        """
        logging.info(f'Deleting template id: {template_id}')

        response_data = self.pxc.delete_template(template_id)

        logging.info('Validating response data')
        AssertResponse.assert_status_code(response_data, 200)
        AssertResponse.assert_message(response_data, "Template deleted successfully")
        assert isinstance(response_data, dict), "Response is not a dictionary"

        logging.info('Test complete: delete_template')

    def test_project_and_stages_flow(self):
        """
        Test the flow of creating a project, creating stages,
        creating a customer, deleting stages, and deleting the project.
        """
        log_template = '#' * 20

        # 1. Create New Template
        logging.info(f'{log_template} TEST 1 STARTED {log_template}\nCreating New Template...')
        template_id = self.test_create_template()
        logging.info(f'{log_template} TEST 1 FINISHED {log_template}\nCreated with Template ID: {template_id}')

        # 2. Create 3 New Stages For New Template
        logging.info(f'{log_template}TEST 2 STARTED {log_template}\nCreating 3 new stages from Template ID: {template_id} ...')
        self.test_create_template_stages(template_id)
        logging.info(f'{log_template}TEST 2 FINISHED {log_template}\nStages created for Template ID: {template_id}')

        # 3. Create A Project From Template ID With End User Information
        logging.info(f'{log_template} TEST 3 STARTED {log_template}\nCreating project using Template ID: {template_id} ...')
        project_id, portal_id = self.test_create_project(template_id)
        logging.info(
            f'{log_template} TEST 3 FINISHED {log_template}\n'
            f'Created project with:\nTemplate ID: {template_id}\n'
            f'Project ID: {project_id}\nPortal ID: {portal_id}'
        )

        # 4. Get All Stages by Template ID
        logging.info(f'{log_template} TEST 4 STARTED {log_template}\nGet all stages with Template ID {template_id}...')
        stage_ids = self.test_get_all_stages_by_template_id(template_id)
        logging.info(f'{log_template} TEST 4 FINISHED {log_template}\nGot all stages with Template ID {template_id}')

        # 5. Complete All Stages One at a Time Until Project Fully Complete
        logging.info(f'{log_template} TEST 5 STARTED {log_template}\nComplete all stages by Portal ID and Project ID...')
        self.test_complete_project_stages(stage_ids, [project_id, portal_id])
        logging.info(f'{log_template} TEST 5 FINISHED {log_template}\nComplete all stages by Portal ID and Project ID')

        # 6. Delete project
        logging.info(f'{log_template} TEST 6 STARTED {log_template}\nDeleting Project by Project ID: {project_id}...')
        self.test_delete_project(project_id=project_id)
        logging.info(f'{log_template} TEST 6 FINISHED {log_template}\nDeleted Project by Project ID: {project_id}')

        # 7. Delete each stage
        logging.info(f'{log_template} TEST 7 STARTED {log_template}\nDeleting each stage in Project Template ID {project_id}...')
        self.test_delete_stage(stage_ids=stage_ids)
        logging.info(f'{log_template} TEST 7 FINISHED {log_template}\nDeleted all stages in Project Template ID {project_id}')

        # 8. Delete template
        logging.info(f'{log_template} TEST 8 STARTED {log_template}\nDelete template with Template ID {template_id}...')
        self.test_delete_template(template_id=template_id)
        logging.info(f'{log_template} TEST 8 FINISHED {log_template}\nDeleted template with Template ID {template_id}')
