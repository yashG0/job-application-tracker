from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from model import ApplicationStatus


class ApplicationSchemaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ApplicationInSchema(ApplicationSchemaBase):
    company: str = Field(max_length=100, min_length=2)
    position: str = Field(max_length=100, min_length=2)
    location: str | None
    job_url: HttpUrl | None
    status: ApplicationStatus = Field(default=ApplicationStatus.wishlist)
    notes: str | None
    resume_path: str | None


class ApplicationOutSchema(ApplicationSchemaBase):
    id: int
    company: str
    position: str
    location: str | None
    job_url: HttpUrl | None
    status: ApplicationStatus
    notes: str | None
    resume_path: str | None
    applied_at: datetime | None
    created_at: datetime
    updated_at: datetime


class ApplicationUpdateSchema(ApplicationSchemaBase):
    company: str | None = None
    position: str | None = None
    location: str | None = None
    notes: str | None = None
    status: ApplicationStatus | None = None


class DashboardStatsSchema(BaseModel):
    total: int
    wishlist: int
    applied: int
    assessment: int
    interview: int
    offer: int
    rejected: int
