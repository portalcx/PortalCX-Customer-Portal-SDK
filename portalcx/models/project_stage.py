#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
project_stage_models.py
-----------------------
Models for project stage related operations.
"""

from typing import Optional
from .base_model import BaseModel


class ProjectStageCreateRequest(BaseModel):
    """
    Represents a request to create a new project stage.
    """
    ProjectStageId: Optional[int] = None
    ProjectId: str
    StageName: str
    StageDescription: str
    StagePromptButtonCopy: Optional[str] = None
    StagePromptButtonUrl: Optional[str] = None
