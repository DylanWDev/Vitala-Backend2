from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class MealLogs(Base):
    __tablename__ = "meal_logs"

    id = Column(Integer, primary_key=True, index=True)
    meal_type = Column(String, index=True)
    portion_size = Column(Integer, index=True)
    log_date = Column(DateTime, index=True)
    calories = Column(Integer, index=True)
    protein = Column(Integer, index=True)
    carbs = Column(Integer, index=True)
    fats = Column(Integer, index=True)
    water = Column(Integer, index=True)

    user_id = ForeignKey("users.id")
    food_id = ForeignKey("api_foods.id")
