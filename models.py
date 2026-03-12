from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    amount = Column(Integer)
    gold_grams = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
