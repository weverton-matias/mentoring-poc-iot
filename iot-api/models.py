from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from db import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    device = Column(String(50))
    ph = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
