#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
models/admin_template_models.py
----------------------
This file contains models for representing Admin Template data.
"""

from __future__ import annotations

from typing import Optional
from .base_model import BaseModel


class CreateTemplate(BaseModel):
    """
    This class represents a template creation request.
    """

    templateId: Optional[str]
    companyId: Optional[int]
    title: str
    contactEmail: str
    contactPhone: str
    companyName: str
    color: Optional[str]
    templateAppLogoUpload: Optional[str]
    emailLogoUpload: Optional[str]
    isCustomerReferrals: bool
    isLogoUpdate: Optional[bool]
    isEmailLogoUpdate: Optional[bool]
    countryId: Optional[int]


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
