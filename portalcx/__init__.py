"""
portalcx/__init__.py
--------------------
This module contains the PortalCX class which serves as the main entry point for the SDK.
"""

from pydantic import ValidationError

from .api.admin_projects import AdminProject
from .api.admin_templates import AdminTemplate
from .api.auth_management import AuthManagement
from .models.admin_project_models import ProjectCreateRequest
from .models.admin_template_models import (CreateTemplate,
                                           GetAllStagesByTemplateIdParams,
                                           TemplateStageCreateRequest)
from .models.auth_management_models import AuthManagementRegister
from .utils.logger import get_logger


class PortalCX:
    """
    Main class for the PortalCX SDK.
    """

    def __init__(self, base_url, auth_token=None):
        """
        Initialize the API base class with base URL and optional authentication token.

        :param base_url: The base URL of the API
        :param auth_token: The authentication token (optional)
        """
        self.base_url = base_url
        self.auth_token = auth_token
        self.logger = get_logger()

        # Initialize API classes with base URL and auth token
        self.auth_management = AuthManagement(base_url)
        self.admin_template = AdminTemplate(base_url, auth_token)
        self.admin_project = AdminProject(base_url, auth_token)

    @property
    def token(self):
        return self.auth_token

    @token.setter
    def token(self, value):
        self.auth_token = value

        # Update the token in the API classes
        self.auth_management.token = value
        self.admin_template.token = value
        self.admin_project.token = value

    # _____________________________  Auth Management Section  _____________________________
    def login(self, email: str, password: str) -> str:
        """
        Logs into the PortalCX API with the provided credentials.

        :param email: The email of the user
        :param password: The password of the user
        :return: The token received from the login operation
        """
        self.token = self.auth_management.login(email, password)
        return self.token

    def register(self, user_data: AuthManagementRegister) -> dict:
        """
        Registers a new user with the provided information.

        :param user_data: A UserRegistration object containing the user information
        :return: The JSON response from the API
        """
        return self.auth_management.register(user_data)

    # _____________________________ Templates Section  _____________________________
    def create_template(self, template_data: CreateTemplate) -> dict:
        """
        Creates a new template with the provided information.

        :param template_data: A CreateTemplateRequest object containing the template information
        :return: The JSON response from the API
        """
        return self.admin_template.create_template_request(template_data)

    def create_template_stage(self, stage_data: TemplateStageCreateRequest) -> dict:
        """
        Creates a new template stage with the provided information.

        :param stage_data: A TemplateStageCreateRequest object containing the stage information
        :return: The JSON response from the API
        """
        return self.admin_template.create_template_stage_request(stage_data)
    
    def get_all_stages_by_template_id(self, template_id: str) -> dict:
        """
        Gets all template stages for a specific template.

        :param template_id: A UUID string of the template
        :return: The JSON response from the API
        """
        try:
            GetAllStagesByTemplateIdParams(templateId=template_id)
        except ValidationError as e:
            self.logger.error(f"Invalid template ID: {template_id}")
            raise e

        return self.admin_template.get_all_stages_by_template_id_request(template_id)

    # _____________________________  Projects Section  _____________________________

    def create_project(self, project_data: ProjectCreateRequest) -> dict:
        """
        Creates a new project with the provided information.

        :param project_data: A ProjectCreateRequest object containing the project information
        :return: The JSON response from the API
        """
        return self.admin_project.create_project_request(project_data)