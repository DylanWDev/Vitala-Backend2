from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime, VARCHAR
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from typing import List
from datetime import datetime
from app.schemas.food_log import FoodLogSchema

from app.db.base_class import Base

class FoodLog(Base):
    __tablename__ = "food_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    meal_type: Mapped[str] = mapped_column(String, index=True)
    servings: Mapped[float] = mapped_column(Float, index=True)
    date_logged: Mapped[datetime] = mapped_column(DateTime, index=True)
    calories: Mapped[float] = mapped_column(Float, index=True)
    protein: Mapped[float] = mapped_column(Float, index=True)
    carbs: Mapped[float] = mapped_column(Float, index=True)
    fats: Mapped[float] = mapped_column(Float, index=True)
    serving_unit: Mapped[str] = mapped_column(VARCHAR, index=True)
    serving_weight_grams: Mapped[int] = mapped_column(Integer, index=True)
    food_name: Mapped[str] = mapped_column(String, index=True)

    food: Mapped[List["UsersToFoods"]] = relationship(back_populates="pivot")



    def to_schema(self):
        return FoodLogSchema(
            id=self.id,
            meal_type=self.meal_type,
            servings=self.servings,
            date_logged=self.date_logged,
            calories=self.calories,
            protein=self.protein,
            carbs=self.carbs,
            fats=self.fats,
            serving_unit=self.serving_unit,
            serving_weight_grams=self.serving_weight_grams,
            food_name=self.food_name
        )