from typing import Optional
from pydantic import BaseModel

class NutritionixSchema(BaseModel):
    external_id: Optional[int] = None
    name: Optional[str] = None
    calories: Optional[int] = None
    servings_size: Optional[int] = None