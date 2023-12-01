from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodLogSchema(BaseModel):
    meal_type: str
    servings: float
    date_logged: datetime
    calories: float
    protein: float
    carbs: float
    fats: float
    water: float
    serving_unit: str
    serving_weight_grams: int

    class Config:
        orm_mode = True

class FoodLogInDBSchema (FoodLogSchema):
    id: int