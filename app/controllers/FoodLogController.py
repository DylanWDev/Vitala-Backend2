from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.models import FoodLog
from app.schemas.food_log import FoodLogSchema, FoodLogInDBSchema
from app.controllers import BaseController

class FoodLogController(BaseController[FoodLog, FoodLogSchema, FoodLogInDBSchema]):
    def create_food_log(self, db: Session = Depends(deps.get_db), *, obj_in: FoodLogSchema) -> FoodLog:
        food_log_obj = FoodLog(
            meal_type=obj_in.meal_type

        )
        db.add(food_log_obj)
        db.commit()
        db.refresh(food_log_obj)
        return food_log_obj
    
flc = FoodLogController(FoodLog)