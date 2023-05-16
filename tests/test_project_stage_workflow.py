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

    def create_template_test(self):
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

    def create_stages(self, project_id: str):
        """
        Creates 3 stages for a given project.

        :param project_id: The id of the project to create stages for
        """
        for i in range(3):
            stage_data = ProjectStageCreateRequest(
                ProjectStageId=None,
                ProjectId=project_id,
                StageName=f"Stage {i+1}",
                StageDescription=f"Description for Stage {i+1}",
                StagePromptButtonCopy=None,
                StagePromptButtonUrl=None
            )

            stage_response_text = self.pxc.create_project_stage(project_stage_data=stage_data)

            assert stage_response_text is not None
            assert isinstance(stage_response_text, str)

    def create_customer(self, project_id: str):
        """
        Creates a customer for a given project.

        :param project_id: The id of the project to create a customer for
        """
        customer_data = PortalCustomerCreateRequest(
            portalCustomerId=None,
            projectId=project_id,
            firstName="Matthew",
            lastName="Schwen",
            email="matt@portalcx.com",
            phoneNumber="1234567899",
            address="some address",
            city="Sandy",
            stateCode="UT",
            zip="84070",
            notifyViaEmail=True,
            notifyViaSMS=True,
            completeFirstStage=False,
            countryId=1
        )

        customer_response = self.pxc.create_customer(customer_data=customer_data)
        
        # customer_response example
        # '{'portalId': '6553d82c-1a8c-4c6a-8d07-c5d4bc9cdbb9',
        # 'message': 'Portal created successfully'}'

        response = json.loads(customer_response)
        assert isinstance(response, dict), "Response is not a dictionary"

        # check keys
        assert "portalId" in response, "Response does not contain 'portalId'"
        assert "message" in response, "Response does not contain 'message'"

        # check values
        assert isinstance(response['portalId'], str), "'portalId' is not a string"
        assert isinstance(response['message'], str), "'message' is not a string"

        # check specific values
        assert re.match(r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$', response['portalId']) is not None
        assert response['message'] == "Portal created successfully", "Unexpected 'message'"

        return response['portalId']

    def complete_all_stages(self, portal_id: str, project_id: str):
        """
        Fetches all stages for a project, and updates each to a completed status. Waits for 10 seconds between each update.

        :param portal_id: The id of the portal
        :param project_id: The id of the project
        """

        # Get all stages
        stages_response = self.pxc.get_all_stages_by_project_id(project_id=project_id)

        # Extract stage ids
        stage_ids = self.extract_stage_ids(stages_response)

        for stage_name, stage_id in stage_ids.items():
            # Create the UpdatePortalStageRequest object
            stage_update_request = UpdatePortalStageRequest(
                portalId=portal_id,
                stageId=None,
                dateCompleted=datetime.datetime.now(),  
                label=stage_name,
            )
            
            # stage_update_request example: UpdatePortalStageRequest(portalId='49852bc1-a99d-4937-be65-dd5dfc813c9a', stageId=None, dateCompleted=datetime.datetime(2023, 5, 15, 14, 53, 3, 437386), label='Stage 1')

            time.sleep(300)

            response = self.pxc.update_project_stage(portal_stage_change_request=stage_update_request)
            
            # response example: 'Portal customer stage changed'
            
            assert isinstance(response, str), "Response is not a string"
            assert response == 'Portal customer stage changed', "Unexpected response message"

            # Wait for 10 seconds
            time.sleep(10)

    def delete_stages(self, project_id: str):
        """
        Deletes all stages for a given project.

        :param project_id: The id of the project to delete stages from
        """
        # Get stage ID's from Project
        stage_ids_response = self.pxc.get_all_stages_by_project_id(project_id=project_id)

        # Extract stage ids
        stage_ids = self.extract_stage_ids(stage_ids_response)

        for stage_id in stage_ids.values():
            delete_stage_response = self.pxc.delete_project_stage(project_stage_id=stage_id)

            assert delete_stage_response is not None
            assert isinstance(delete_stage_response, str)
            assert delete_stage_response == 'Project Stage deleted successfully'

    def delete_project(self, project_id: str):
        """
        Deletes a given project.

        :param project_id: The id of the project to delete
        """
        delete_project_response = self.pxc.delete_project(project_id=project_id)

        assert delete_project_response is not None
        assert isinstance(delete_project_response, str)
        assert delete_project_response == 'Project deleted successfully'

    def test_project_and_stages_flow(self):
        """
        Test the flow of creating a project, creating stages,
        creating a customer, deleting stages, and deleting the project.
        """

        # 1. Create a project
        project_id = self.create_template_test()
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

