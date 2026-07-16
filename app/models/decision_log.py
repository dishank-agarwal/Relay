from sqlalchemy import Boolean, Column, Float, DateTime, Integer, String
from datetime import datetime

from app.database.database import Base

class DecisionLog(Base):
    __tablename__ = "decision_logs"

    id = Column(Integer, primary_key=True, index=True)

    merchant_id = Column(String)
    transaction_id = Column(String)

    action = Column(String)
    amount = Column(Float)

    decision = Column(String)
    reason = Column(String)

    risk_score = Column(Integer)
    policy = Column(String)

    can_execute = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)