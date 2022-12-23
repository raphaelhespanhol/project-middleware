from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, Date, Time

Base = declarative_base()
metadata = Base.metadata

class Status(Base):

    __tablename__ = "status"

    id = Column(Integer(),primary_key=True)
    active = Column(Boolean(), default=True)
    date = Column(Date, nullable=False)
    hour = Column(Time, nullable=False)