from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime, VARCHAR
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.schemas import UserInDB
from typing import List

from app.db.base_class import Base

class FoodLog(Base):
    __tablename__ = "meal_logs"

    id = Column(Integer, primary_key=True, index=True)
    meal_type = Column(String, index=True)
    servings = Column(Float, index=True)
    date_logged = Column(DateTime, index=True)
    calories = Column(Float, index=True)
    protein = Column(Float, index=True)
    carbs = Column(Float, index=True)
    fats = Column(Float, index=True)
    water = Column(Float, index=True)
    serving_unit = Column(VARCHAR, index=True)
    serving_weight_grams = Column(Integer, index=True)

    food: Mapped[List["UsersToFoods"]] = relationship(back_populates="pivot")




    class UsersToFoods(Base):
        __tablename__ = "users_to_foods"

        id: Mapped[int] = mapped_column(primary_key=True, index=True)
        user_id: Mapped[int] = mapped_column(ForeignKey(user.id))
        food_id: Mapped[int] = mapped_column(ForeignKey(food_log.id))

        user: Mapped[List["User"]] = relationship(back_populates="pivot")
        pivot: Mapped[List["FoodLog"]] = relationship(back_populates="food")