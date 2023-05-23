#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
models/admin_template_models.py
----------------------
This file contains models for representing Admin Template data.
"""

from __future__ import annotations

from enum import IntEnum
from typing import List, Optional

from .base_model import BaseModel


class ProjectCreateRequest(BaseModel):
    """
    This class represents a request to create a project.
    """
    projectId: Optional[int]
    templateId: str
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    addressLine1: Optional[str]
    addressLine2: Optional[str]
    city: Optional[str]
    stateCode: Optional[str]
    zip: Optional[str]
    notifyViaEmail: bool
    notifyViaSMS: bool
    completeFirstStage: bool
    countryId: int
    #projectSubscribers: Optional[List[ProjectSubscriberRequestViewModel]]


class GetProjectDetailViewModel(BaseModel):
    """
    This class represents the details of a project.
    """
    projectId: int
    status: ProjectStatusEnum
    firstName: Optional[str]
    lastName: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    addressLine1: Optional[str]
    addressLine2: Optional[str]
    city: Optional[str]
    stateCode: Optional[str]
    zip: Optional[str]
    notifyViaEmail: bool
    notifyViaSMS: bool
    countryId: Optional[int]
    projectSubscribers: Optional[List[ProjectSubscriberRequestViewModel]]
    deletedProjectSubscriberIds: Optional[List[int]]


class ProjectSubscriberRequestViewModel(BaseModel):
    """
    This class represents a request to subscribe to a project.
    """
    projectSubscriberId: int
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    notifyViaEmail: bool
    notifyViaSMS: bool
    countryId: int


class ProjectStatusEnum(IntEnum):
    """
    This class represents the possible statuses of a project.
    """
    STATUS_0 = 0
    STATUS_1 = 1
    STATUS_2 = 2
