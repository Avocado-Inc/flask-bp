from sqlalchemy import Boolean, Column, Integer, String
from .database import Base




class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

