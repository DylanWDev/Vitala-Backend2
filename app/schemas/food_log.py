from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodLogBase(BaseModel):
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

class FoodLogInDBBase (FoodLogBase):
   id: int

class FoodLogUpdate (FoodLogBase):
    meal_type: str
    servings: float
    calories: float
    protein: float
    carbs: float
    fats: float
    water: float
    serving_unit: str
    serving_weight_grams: int


class FoodLogSchema(FoodLogInDBBase):

   class Config:
      from_attributes = True

      allow_population_by_field_name = True