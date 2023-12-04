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
            date_logged=obj_in.date_logged,
            calories=obj_in.calories,
            protein=obj_in.protein,
            carbs=obj_in.carbs,
            fats = obj_in.fats,
            water=obj_in.water,
            serving_unit=obj_in.serving_unit,
            serving_weight_grams=obj_in.serving_weight_grams

        )
        db.add(food_log_obj)
        db.commit()
        db.refresh(food_log_obj)
        return food_log_obj
    

    
    
flc = FoodLogController(FoodLog)