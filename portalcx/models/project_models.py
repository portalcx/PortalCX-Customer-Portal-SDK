#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
project_models.py
-----------------
Models for project related operations.
"""

from typing import Optional, List
from .base_model import BaseModel

class CreateProjectRequest(BaseModel):
    """
    Represents a request to create a new project.
    """
    ProjectId: Optional[str] = None
    CompanyId: Optional[str] = None
    Title: str
    ContactEmail: str
    ContactPhone: str
    CompanyName: str
    Color: Optional[str] = None
    PortalAppLogoUpload: Optional[str] = None
    EmailLogoUpload: Optional[str] = None
    IsCustomerReferrals: bool
    IsLogoUpdate: Optional[bool] = None
    IsEmailLogoUpdate: Optional[bool] = None
    CountryId: Optional[int] = None
