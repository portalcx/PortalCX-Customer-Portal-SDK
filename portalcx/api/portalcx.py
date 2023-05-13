#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/portalcx.py
---------------
Class representing the PortalCX API.
"""

import json
from typing import Union
from uuid import UUID

from ..models.register_customer import CustomerData
from ..models.project import CreateProjectRequest
from ..models.project_stage import ProjectStageCreateRequest
from ..utils.logger import get_logger
from .api_base import APIBase


class PortalCX(APIBase):
    """
    Class representing the PortalCX API.
    """

    def __init__(self, api_base_url: str):
        super().__init__(api_base_url)
        self.logger = get_logger()
        self._token = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def register(self, user_data: CustomerData) -> dict:
        """
        Registers a new user with the provided information.

        :param user_data: A UserRegistration object containing the user information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        register_url = "/api/AuthManagement/Register"
        self.logger.info(f"Registering a new user with email: {user_data.email}")
        response_data = self.request("POST", register_url, json=user_data.dict())
        self.logger.info("Successfully registered a new user")

        return response_data

    def login(self, email: str, password: str) -> str:
        """
        Logs into the PortalCX API with the provided credentials.
        """
        login_url = "/api/AuthManagement/Login"
        body = {"email": email, "password": password}
        self.logger.info(f"Logging into PortalCX API with email: {email}")
        response_data = self.request("POST", login_url, json=body)
        self.token = response_data.get("token")
        self.logger.info("Successfully logged into PortalCX API")

        return self.token

    def create_project(self, project_data: CreateProjectRequest) -> dict:
        """
        Creates a new project with the provided data.

        :param project_data: A CreateProjectRequest object containing the project data
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        create_project_url = "/api/Admin/Project/CreateProject"
        headers = {'Authorization': f'Bearer {self.token}'}
        self.logger.info("Creating a new project")
        project_data_dict = project_data.to_dict()
        self.logger.info(f"Using the following data to Create Project: \n{json.dumps(project_data_dict, indent=4)}")

        # Prepare multipart/form-data body
        multipart_data = {key: ('', str(value)) for key, value in project_data_dict.items()}

        response_data = self.request("POST", create_project_url, files=multipart_data, headers=headers)

        return response_data

    def delete_project(self, project_id: Union[str, UUID]) -> None:
        """
        Delete a project.

        :param project_id: The UUID of the project to delete
        :return: None
        :raise: APIBaseError if the request fails
        """
        delete_project_url = "/api/Admin/Project/DeleteProject"
        headers = {'Authorization': f'Bearer {self.token}'}
        self.logger.info(f"Deleting the project with ID: {project_id}")
        params = {'projectId': str(project_id)}

        response_data = self.request("DELETE", delete_project_url, params=params, headers=headers)

        return response_data

    def create_project_stage(self, project_stage_data: ProjectStageCreateRequest) -> int:
        """
        Creates a new project stage with the provided data.

        :param project_stage_data: A ProjectStageCreateRequest object containing the project stage data
        :return: The ID of the newly created project stage
        :raise: APIBaseError if the request fails
        """
        create_stage_url = "/api/Admin/Project/CreateStage"
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        self.logger.info("Creating a new project stage")

        # Convert the project stage data to a dictionary and then to a JSON string
        stage_data_json = json.dumps(project_stage_data.to_dict())
        self.logger.info(f"Using the following data to Create Project Stage: \n{json.dumps(project_stage_data.to_dict(), indent=4)}")

        response_data = self.request("POST", create_stage_url, content=stage_data_json, headers=headers)

        return response_data
    
    def get_all_stages_by_project_id(self, project_id: str) -> dict:
        """
        Fetches all the stages of a project with the provided project ID.

        :param project_id: A string containing the project ID
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        get_stages_url = "/api/Admin/Project/GetAllStagesByProjectId"
        headers = {'Authorization': f'Bearer {self.token}'}
        params = {'projectId': project_id}
        self.logger.info(f"Fetching all stages for the project: {project_id}")

        response_data = self.request("GET", get_stages_url, params=params, headers=headers)

        return response_data


    def delete_project_stage(self, project_stage_id: int) -> None:
        """
        Delete a project stage.

        :param project_stage_id: The ID of the project stage to delete
        :return: None
        :raise: APIBaseError if the request fails
        """
        delete_project_stage_url = "/api/Admin/Project/DeleteStage"
        headers = {'Authorization': f'Bearer {self.token}'}
        self.logger.info(f"Deleting the project stage with ID: {project_stage_id}")
        params = {'projectStageId': project_stage_id}

        response_data = self.request("DELETE", delete_project_stage_url, params=params, headers=headers)

        return response_data
