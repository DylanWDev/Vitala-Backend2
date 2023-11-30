from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped
from app.schemas import UserInDB
from typing import List

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    age = Column(Integer, index=True)
    weight = Column(Float, index=True)
    height = Column(Float, index=True)
    gender = Column(String, index=True)
    activity_level = Column(Integer, index=True)

    pivot: Mapped[List["UsersToFoods"]] = relationship(back_populates="users")

    relationship()

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser
        )