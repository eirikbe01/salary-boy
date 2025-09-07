from typing import Optional, Literal
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from .salary import Gender, JobType

class PredictRequest(BaseModel):
    """What the client sends to /predict endpoint: all features except reported_salary
    """
    gender: Optional[Gender] = None
    years_education: Optional[int] = Field(default=None, ge=0, le=60)
    years_experience: Optional[int] = Field(default=None, ge=0, le=60)
    region: Optional[str] = None
    job_type: Optional[JobType] = None
    specialization: Optional[str] = None
    reported_salary: Optional[int] = Field(default=None, ge=0)
    includes_bonus: Optional[bool] = None
    includes_provision: Optional[bool] = None

class ReferenceGroupStats(BaseModel):
    count: int
    average: Optional[float] = None
    median: Optional[float] = None
    p95: Optional[float] = None

class PredictResponse(BaseModel):
    """What /predict endpoint returns as response"""
    predicted_salary: int
    model_version: str
    confidence_band: Optional[int] = None
    reference_group_stats: Optional[ReferenceGroupStats] = None


# Schemas for logging each prediction (more training data)
class PredictionLogCreate(PredictRequest):
    predicted_salary: int
    model_version: str
    actual_salary: Optional[int] = None

class PredictionLogResponse(PredictionLogCreate):
    id: int
    create_at: datetime
    model_config = ConfigDict(from_attributes=True)