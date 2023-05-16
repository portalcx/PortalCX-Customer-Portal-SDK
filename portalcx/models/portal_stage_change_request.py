#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
portal_stage_change_request.py
-------------------------------
Models for portal stage change request operations.
"""

from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdatePortalStageRequest(BaseModel):
    """
    A model representing a request to update a Portal Stage. This model extends
    the BaseModel and provides fields specific to the Portal Stage update operation.

    Attributes:
        portalId: A string that represents the Portal's unique identifier. This is a required field.
        stageId: An optional integer that represents the Stage's unique identifier.
        dateCompleted: A datetime object representing the date and time when the Stage was completed.
        label: A string representing the label of the Stage. This is a required field.
    """
    portalId: str = Field(..., min_length=1)
    stageId: Optional[int]
    dateCompleted: datetime
    label: str = Field(..., min_length=1)

    def to_dict(self) -> Dict[str, Any]:
        output_dict = super().to_dict()
        output_dict["dateCompleted"] = self.dateCompleted.isoformat()
        return output_dict
