from sqlalchemy import Boolean, Column, Integer, String

from app.database.database import Base


class Policy(Base):

    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)

    policy_id = Column(String, unique=True)

    rule = Column(String)

    priority = Column(Integer)

    enabled = Column(Boolean, default=True)