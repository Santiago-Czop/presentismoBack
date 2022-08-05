from sqlalchemy import Column, Integer, DateTime

from database import Base

class Presente(Base):
    __tablename__ = 'presente'
    legajo = Column(Integer, primary_key=True)
    fecha = Column(DateTime, primary_key=True)