from typing import Optional, Literal
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class Gender(str, Enum):
    male = "male"
    female = "female"

class JobType(str, Enum):
    IN_HOUSE_PRIVATE = "IN_HOUSE_PRIVATE"
    IN_HOUSE_PUBLIC = "IN_HOUSE_PUBLIC"
    CONSULTANT = "CONSULTANT"
    FREELANCE = "FREELANCE"

# Parent class
class SalaryBase(BaseModel):
    gender: Optional[Gender] = None
    years_education: Optional[int] = Field(default=None, ge=0, le=60)
    years_experience: Optional[int] = Field(default=None, ge=0, le=60)
    region: Optional[str] = None
    job_type: Optional[JobType] = None
    specialization: Optional[str] = None
    reported_salary: Optional[int] = Field(default=None, ge=0)
    includes_bonus: Optional[bool] = None
    includes_provision: Optional[bool] = None

# Request body when creating a new record
class SalaryCreate(SalaryBase):
    # salary required by clients to send
    reported_salary: int = Field(ge=0)
    includes_bonus: bool = False
    includes_provision: bool = False

class SalaryUpdate(SalaryBase):
    pass

class SalaryResponse(SalaryBase):
    id: int # database-generated
    reported_salary: int
    includes_bonus: bool
    includes_provision: bool
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

