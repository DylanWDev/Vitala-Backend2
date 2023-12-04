from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodLogBase(BaseModel):
    meal_type: Optional[str] = None
    servings: Optional[float] = None
    date_logged: Optional[datetime] = None
    calories: Optional[float] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None
    water: Optional[float] = None
    serving_unit: Optional[str] = None
    serving_weight_grams: Optional[int] = None

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