from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, JSON, Index, text

from db.database import Base

class ModelArtifact(Base):
    __tablename__ = "model_artifacts"

    id = Column(Integer, primary_key=True)
    version = Column(String, unique=True, nullable=False)
    trained_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    features = Column(JSON, nullable=True)
    metrics = Column(JSON, nullable=True)
    notes = Column(JSON, nullable=True)


# Log each prediction request/response
class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # same feature columns as PredictInput (no reported_salary)
    gender = Column(String(16), nullable=True)
    years_education = Column(Integer, nullable=True)
    years_experience = Column(Integer, nullable=True)
    region = Column(String(64), nullable=True)
    job_type = Column(String(32), nullable=True)
    specialization = Column(String(64), nullable=True)
    includes_bonus = Column(Boolean, nullable=False, default=False, server_default=text("false"))
    includes_provision = Column(Boolean, nullable=False, default=False, server_default=text("false"))

    # prediction & version
    predicted_salary = Column(Integer, nullable=False)
    model_version = Column(String(64), nullable=False)

    # feedback (optional, if user later provides actual salary)
    actual_salary = Column(Integer, nullable=True)