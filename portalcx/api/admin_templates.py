#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api/admin_templates.py
----------------------
This module represents all API calls in the /api/Admin/Template section.
"""

from typing import Dict

from portalcx.models.admin_template_models import (
    CreateTemplate,
    TemplateStageCreateRequest,
    ProjectStageCompleteRequest
)

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

        self.logger.info(f"Creating a new template stage with name: {stage_data.stageName} for template id: {stage_data.templateId}")

        # Convert to JSON
        stage_data_dict = stage_data.to_dict()

        # Make the request and process the response
        response_data = self.request("POST",
                                     create_stage_url,
                                     json=stage_data_dict,
                                     headers=headers)

        self.logger.info("Successfully created a new template stage")

        return response_data

    def get_all_stages_by_template_id_request(self, template_id: str) -> Dict:
        """
        Gets all template stages for a specific template.

        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        headers = {'Authorization': f'Bearer {self.token}'}

        get_stages_url = f"/api/Admin/Template/GetAllStagesByTemplateId?templateId={template_id}"

        self.logger.info(f"Getting all stages for Template Id: {template_id}")
    
        # Make the request and process the response
        response_data = self.request("GET", get_stages_url, headers=headers)
        
        self.logger.info("Successfully retrieved template stages")

        return response_data

    def complete_project_stage_request(self, complete_stage_data: ProjectStageCompleteRequest) -> Dict:
        """
        Complete a project stage.

        :param complete_stage_data: A ProjectStageCompleteRequest object containing the stage information
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        complete_stage_url = "/api/Admin/Project/CompleteProjectStage"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Setting stage {complete_stage_data.completedStageLabel} to Complete")

        # Convert to JSON
        complete_stage_data_dict = complete_stage_data.to_dict()

        # Make the request and process the response
        response_data = self.request("POST",
                                     complete_stage_url,
                                     json=complete_stage_data_dict,
                                     headers=headers)

        self.logger.info(f"Successfully completed stage: {complete_stage_data.completedStageLabel}")

        return response_data

    def delete_stage_request(self, template_stage_id: int) -> Dict:
        """
        Delete a stage.

        :param template_stage_id: An integer containing the stage id
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        delete_stage_url = f"/api/Admin/Template/DeleteStage?templateStageId={template_stage_id}"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Deleting stage with id: {template_stage_id}")

        # Make the request and process the response
        response_data = self.request("DELETE", delete_stage_url, headers=headers)

        self.logger.info(f"Successfully deleted stage: {template_stage_id}")

        return response_data

    def delete_template_request(self, template_id: str) -> Dict:
        """
        Delete a template.

        :param template_id: A UUID string containing the template id
        :return: The JSON response from the API
        :raise: APIBaseError if the request fails
        """
        delete_template_url = f"/api/Admin/Template/DeleteTemplate?templateId={template_id}"
        headers = {'Authorization': f'Bearer {self.token}'}

        self.logger.info(f"Deleting template with id: {template_id}")

        # Make the request and process the response
        response_data = self.request("DELETE", delete_template_url, headers=headers)

        self.logger.info(f"Successfully deleted template: {template_id}")

        return response_data