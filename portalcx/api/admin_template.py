#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/admin_template.py
----------------------
This module represents all API calls in the /api/Admin/Template section.
"""

from typing import Dict

from portalcx.models.admin_template_models import CreateTemplate, TemplateStageCreateRequest
from .api_base import APIBase


class AdminTemplate(APIBase):
    """
    Class for managing template-related operations.
    """

    def __init__(self, base_url: str, token: str = None):
        super().__init__(base_url)
        self.token = token

    def create_template_request(self, template_data: CreateTemplate) -> Dict:
        """
        Creates a new template with the provided information.

        :param template_data: A CreateTemplateRequest object containing the template information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        create_template_url = "/api/Admin/Template/CreateTemplate"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Creating a new template with title: {template_data.title}")

        # Convert to JSON
        template_data_dict = template_data.to_dict()

        # Prepare multipart/form-data body
        multipart_data = {key: ('', str(value)) for key, value in template_data_dict.items()}

        # Make the request and process the response
        response_data = self.request("POST",
                                     create_template_url,
                                     files=multipart_data,
                                     headers=headers)
        
        self.logger.info("Successfully created a new template")

        return response_data

    def create_template_stage_request(self, stage_data: TemplateStageCreateRequest) -> Dict:
        """
        Creates a new template stage with the provided information.

        :param stage_data: A TemplateStageCreateRequest object containing the stage information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        create_stage_url = "/api/Admin/Template/CreateStage"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Creating a new template stage with name: {stage_data.stageName}")

        # Convert to JSON
        stage_data_dict = stage_data.to_dict()

        # Make the request and process the response
        response_data = self.request("POST",
                                     create_stage_url,
                                     json=stage_data_dict,
                                     headers=headers)

        self.logger.info("Successfully created a new template stage")

        return response_data
