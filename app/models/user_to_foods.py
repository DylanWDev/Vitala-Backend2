from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime, VARCHAR
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.schemas import UserInDB
from typing import List
from app.db.base_class import Base


class UsersToFoods(Base):
        __tablename__ = "users_to_foods"

        id: Mapped[int] = mapped_column(primary_key=True, index=True)
        user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
        food_id: Mapped[int] = mapped_column(ForeignKey("food_log.id"))

        users: Mapped[List["User"]] = relationship(back_populates="pivot")
        pivot: Mapped[List["FoodLog"]] = relationship(back_populates="food")