from sqlalchemy import Column, Integer, String, Boolean

from db.database import Base

class SalaryRecord(Base):
    __tablename__ = "salary_records"
    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    years_education = Column(Integer)
    years_experience = Column(Integer)
    region = Column(String)
    job_type = Column(String)
    specialization = Column(String)
    reported_salary = Column(Integer)
    includes_bonus = Column(Boolean)
    includes_provision = Column(Boolean)

