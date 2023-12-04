from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import FoodLog
from app.schemas import FoodLogSchema, FoodLogInDBBase, FoodLogUpdate
from app.controllers.BaseController import BaseController

class FoodLogController(BaseController[FoodLog, FoodLogInDBBase, FoodLogUpdate]):
    def create(self, db: Session, *, obj_in: FoodLogInDBBase) -> FoodLog:
        food_log_obj = FoodLog(
            meal_type=obj_in.meal_type,
            servings=obj_in.servings,


        )
        db.add(food_log_obj)
        db.commit()
        db.refresh(food_log_obj)
        return food_log_obj
    
flc = FoodLogController(FoodLog)