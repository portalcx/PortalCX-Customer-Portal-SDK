#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tests/test_project_stage_workflow.py
------------------------------------
Unit tests for the workflow involving project and stage creation/deletion in the PortalCX API class.
"""

import re

from portalcx.models.project import CreateProjectRequest
from portalcx.models.project_stage import ProjectStageCreateRequest
from tests.base_test import BaseTest


class TestProjectAndStagesFlow(BaseTest):
    
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

    def create_project(self):
        """
        Creates a project and returns its ID.
        """
        project_data = CreateProjectRequest(
            ProjectId=None,
            CompanyId=None,
            Title="Solar Installation",
            ContactEmail="projectmanager@solarcompany.com",
            ContactPhone="1234567890",
            CompanyName="Solar Company",
            Color=None,
            PortalAppLogoUpload=None,
            EmailLogoUpload=None,
            IsCustomerReferrals=True,
            IsLogoUpdate=None,
            IsEmailLogoUpdate=None,
            CountryId=1
        )

        project_id = self.pxc.create_project(project_data=project_data)

        assert project_id is not None
        assert isinstance(project_id, str)
        assert re.match(r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$', project_id) is not None

        return project_id

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
        Test the flow of creating a project, creating stages, deleting stages, and deleting the project.
        """
        # 1. Create a project
        project_id = self.create_project()

        # 2. Create 3 stages for the project
        self.create_stages(project_id)

        # NEED TO ADD STEP TO CREATE A PROJECT BASED OFF THE TEMPLATE AND MOVE FROM START TO FINISH

        # 3. Delete each stage from the project.
        self.delete_stages(project_id)

        # 4. Delete the project
        self.delete_project(project_id)
