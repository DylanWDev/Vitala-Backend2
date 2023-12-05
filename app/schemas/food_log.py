from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodLogBase(BaseModel):
    meal_type: Optional[int] = None
    servings: Optional[float] = None
    date_logged: Optional[datetime] = None
    calories: Optional[float] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None
    serving_unit: Optional[str] = None
    serving_weight_grams: Optional[int] = None

class FoodLogInDBBase (FoodLogBase):
   id: int

class FoodLogUpdate (FoodLogBase):
    meal_type: int
    servings: float
    calories: float
    protein: float
    carbs: float
    fats: float
    serving_unit: str
    serving_weight_grams: int


class FoodLogSchema(FoodLogInDBBase):

   class Config:
      from_attributes = True

      populate_by_name = True