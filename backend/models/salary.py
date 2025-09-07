from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from db.database import Base

class SalaryRecord(Base):
    __tablename__ = "salary_records"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String, nullable=True)
    years_education = Column(Integer, nullable=True)
    years_experience = Column(Integer, nullable=True)
    region = Column(String, nullable=True)
    job_type = Column(String, nullable=True)
    specialization = Column(String, nullable=True)

    reported_salary = Column(Integer, nullable=False)
    includes_bonus = Column(Boolean, nullable=False, default=False, server_default="0")
    includes_provision = Column(Boolean, nullable=False, default=False, server_default="0")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

