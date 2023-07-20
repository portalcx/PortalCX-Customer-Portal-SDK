#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
models/admin_template_models.py
----------------------
This file contains models for representing Admin Template data.
"""

from __future__ import annotations

from typing import Optional, List
from uuid import UUID

from pydantic import constr, root_validator

from .base_model import BaseModel


class CreateTemplate(BaseModel):
    """
    This class represents a template creation request.
    """
    templateId: Optional[str]
    companyId: Optional[int]
    templateName: str
    projectTitle: str
    supportEmailAddress: str
    supportPhoneNumber: str
    companyName: str
    projectAppBrandColor: Optional[str]
    projectForgroundColor: Optional[str]
    templateAppLogoUpload: Optional[str]
    emailLogoUpload: Optional[str]
    isCallToAction: Optional[bool]
    linkText: Optional[str]
    linkUrl: Optional[str]
    projectCompletedMessage: Optional[str]
    isCustomerReferrals: bool
    customerReferralMessage: Optional[str]
    isLogoUpdate: Optional[bool]
    isEmailLogoUpdate: Optional[bool]
    countryId: Optional[int]
    projectOwners: Optional[List[str]]


class TemplateStageCreateRequest(BaseModel):
    """
    This class represents a template stage creation request.
    """
    templateStageId: Optional[str]
    templateId: str
    stageName: str
    stageDescription: str
    stagePromptButtonCopy: Optional[str]
    stagePromptButtonUrl: Optional[str]


class GetAllStagesByTemplateIdParams(BaseModel):
    """
    This class represents the parameters for the 'GetAllStagesByTemplateId' API endpoint.
    """
    templateId: Optional[str]


class ProjectStageCompleteRequest(BaseModel):
    projectId: Optional[int]
    portalId: Optional[str]
    completedStageLabel: str
    completedDate: str
    notifyViaEmail: bool
    notifyViaSms: bool

    @root_validator
    def check_ids(cls, values):
        """
        Validator to ensure that either projectId or portalId is provided, but not both.

        :param cls: The class being validated
        :param values: The values of all fields in the model
        :return: The provided value for either projectId or portalId
        :raises ValueError: If neither projectId nor portalId is provided, or if both are provided
        """
        project_id = values.get('projectId')
        portal_id = values.get('portalId')

        if project_id is None and portal_id is None:
            raise ValueError('Either projectId or portalId must be provided.')

        if project_id is not None and portal_id is not None:
            raise ValueError('Only one of projectId or portalId should be provided.')

        return values