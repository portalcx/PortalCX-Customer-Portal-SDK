#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/admin_projects.py
----------------------
This module represents all API calls in the /api/Admin/Project section.
"""

from typing import Dict

from portalcx.models.admin_project_models import ProjectCreateRequest
from .api_base import APIBase


class AdminProject(APIBase):
    """
    Class for managing template-related operations.
    """

    def __init__(self, base_url: str, token: str = None):
        super().__init__(base_url)
        self.token = token
        
    def create_project_request(self, project_data: ProjectCreateRequest) -> Dict:
        """
        Creates a new project with the provided information.

        :param project_data: A CreateProject object containing the project information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        create_project_url = "/api/Admin/Project/CreateProject"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(
            f"Creating a new project for {project_data.firstName} {project_data.lastName}"
            f" and phone number {project_data.phoneNumber} using the template id:"
            f" {project_data.templateId}"
        )

        # Convert to JSON
        project_data_dict = project_data.to_dict()

        # Make the request and process the response
        response_data = self.request("POST",
                                    create_project_url,
                                    json=project_data_dict,
                                    headers=headers)

        self.logger.info("Successfully created a new project")

        return response_data

    def delete_project_request(self, project_id: int) -> Dict:
        """
        Delete a project.

        :param project_id: An integer containing the project id
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        delete_project_url = f"/api/Admin/Project/DeleteProject?projectId={project_id}"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Deleting project with id: {project_id}")

        # Make the request and process the response
        response_data = self.request("DELETE", delete_project_url, headers=headers)

        self.logger.info(f"Successfully deleted project: {project_id}")

        return response_data
