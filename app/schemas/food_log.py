from pydantic import BaseModel
from datetime import datetime

class FoodLogSchemas(BaseModel):
    id: int
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