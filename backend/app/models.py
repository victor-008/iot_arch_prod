from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime
from .database import Base

class Device(Base):
    __tablename__="devices"
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)

class Telemetry(Base):
    __tablename__="telemetry"
    id=Column(Integer,primary_key=True)
    device_id=Column(Integer)
    temperature=Column(Float)
    humidity=Column(Float)
    timestamp=Column(DateTime,default=datetime.utcnow)
