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

from ..utils.logger import get_logger

from ..models.customer_data_registration import CustomerData
from ..models.project_models import CreateProjectRequest
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