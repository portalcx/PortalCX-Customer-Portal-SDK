

# def delete_project(self, project_id: Union[str, UUID]) -> None:
#     """
#     Delete a project.

#     :param project_id: The UUID of the project to delete
#     :return: None
#     :raise: APIBaseError if the request fails
#     """
#     delete_project_url = "/api/Admin/Project/DeleteProject"
#     headers = {'Authorization': f'Bearer {self.token}'}
#     self.logger.info(f"Deleting the project with ID: {project_id}")
#     params = {'projectId': str(project_id)}

#     response_data = self.request("DELETE", delete_project_url, params=params, headers=headers)

#     return response_data

# def create_project_stage(self, project_stage_data: ProjectStageCreateRequest) -> int:
#     """
#     Creates a new project stage with the provided data.

#     :param project_stage_data: A ProjectStageCreateRequest object containing the project stage data
#     :return: The ID of the newly created project stage
#     :raise: APIBaseError if the request fails
#     """
#     create_stage_url = "/api/Admin/Project/CreateStage"
#     headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
#     self.logger.info("Creating a new project stage")

#     # Convert the project stage data to a dictionary and then to a JSON string
#     stage_data_json = json.dumps(project_stage_data.to_dict())
#     self.logger.info(f"Using the following data to Create Project Stage: \n{json.dumps(project_stage_data.to_dict(), indent=4)}")

#     response_data = self.request("POST", create_stage_url, content=stage_data_json, headers=headers)

#     return response_data

# def get_all_stages_by_project_id(self, project_id: str) -> dict:
#     """
#     Fetches all the stages of a project with the provided project ID.

#     :param project_id: A string containing the project ID
#     :return: The JSON response from the API
#     :raise: APIBaseError if the request fails
#     """
#     get_stages_url = "/api/Admin/Project/GetAllStagesByProjectId"
#     headers = {'Authorization': f'Bearer {self.token}'}
#     params = {'projectId': project_id}
#     self.logger.info(f"Fetching all stages for the project: {project_id}")

#     response_data = self.request("GET", get_stages_url, params=params, headers=headers)

#     return response_data

# def delete_project_stage(self, project_stage_id: int) -> None:
#     """
#     Delete a project stage.

#     :param project_stage_id: The ID of the project stage to delete
#     :return: None
#     :raise: APIBaseError if the request fails
#     """
#     delete_project_stage_url = "/api/Admin/Project/DeleteStage"
#     headers = {'Authorization': f'Bearer {self.token}'}
#     self.logger.info(f"Deleting the project stage with ID: {project_stage_id}")
#     params = {'projectStageId': project_stage_id}

#     response_data = self.request("DELETE", delete_project_stage_url, params=params, headers=headers)

#     return response_data

# def create_customer(self, customer_data: PortalCustomerCreateRequest) -> dict:
#     """
#     Creates a new customer with the provided data.

#     :param customer_data: A PortalCustomerCreateRequest object containing the customer data
#     :return: The JSON response from the API
#     :raise: APIBaseError if the request fails
#     """
#     create_customer_url = "/api/Admin/Customer/create"
#     headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
#     self.logger.info("Creating a new customer")

#     # Convert the customer data to a dictionary and then to a JSON string
#     customer_data_json = json.dumps(customer_data.to_dict())
#     self.logger.info(f"Using the following data to Create Customer: \n{json.dumps(customer_data.to_dict(), indent=4)}")

#     response_data = self.request("POST", create_customer_url, content=customer_data_json, headers=headers)

#     return response_data

# def update_project_stage(self, portal_stage_change_request: UpdatePortalStageRequest) -> dict:
#     """
#     Updates a project stage to completed status.

#     :param portal_stage_change_request: A PortalStageChangeRequest object containing the stage update data
#     :return: The JSON response from the API
#     :raise: APIBaseError if the request fails
#     """
#     update_stage_url = "/api/Admin/Portal/StageChange"
#     headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
#     self.logger.info("Updating a project stage to completed status")

#     stage_data_json = json.dumps(portal_stage_change_request.to_dict())

#     self.logger.info(f"Using the following data to Update Project Stage: \n{portal_stage_change_request.json(indent=4)}")

#     response_data = self.request("POST", update_stage_url, content=stage_data_json, headers=headers)

#     return response_data
