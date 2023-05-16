"""
portalcx/__init__.py
--------------------
This module contains the PortalCX class which serves as the main entry point for the SDK.
"""

from .api.admin_template import AdminTemplate
from .api.auth_management import AuthManagement
from .models.auth_management_models import AuthManagementRegister
from .models.admin_template_models import CreateTemplate
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

    @property
    def token(self):
        return self.auth_token

    @token.setter
    def token(self, value):
        self.auth_token = value
        # Update the token in the API classes
        self.auth_management.token = value
        self.admin_template.token = value

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

    def create_template(self, template_data: CreateTemplate) -> dict:
        """
        Creates a new template with the provided information.

        :param template_data: A CreateTemplateRequest object containing the template information
        :return: The JSON response from the API
        """
        return self.admin_template.create_template_request(template_data)
