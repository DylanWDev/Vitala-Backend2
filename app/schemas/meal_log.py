from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MealLogSchema(BaseModel):
    meal_type: Optional[int] = None
    portion_size: Optional[int] = None
    log_date: Optional[datetime] = None
    calories: Optional[int] = None
    protein: Optional[int] = None
    carbs: Optional[int] = None
    fats: Optional[int] = None
    water: Optional[int] = None