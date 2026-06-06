from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as sql_enum
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ApplicationStatus(str, Enum):
    wishlist = "Wishlist"
    applied = "Applied"
    assessment = "Assessment"
    interview = "Interview"
    offer = "Offer"
    rejected = "Rejected"


class Application(Base):
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(primary_key=True)
    company: Mapped[str] = mapped_column(String(50), nullable=False)
    position: Mapped[str] = mapped_column(String(50))
    location: Mapped[str | None]
    job_url: Mapped[str | None]
    status: Mapped[ApplicationStatus] = mapped_column(
        sql_enum(ApplicationStatus), default=ApplicationStatus.wishlist
    )
    notes: Mapped[str | None]
    resume_path: Mapped[str | None]
    applied_at: Mapped[datetime | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now
    )
