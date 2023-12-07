from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import FoodLog, UsersToFoods

from app.schemas import FoodLogInDBBase, FoodLogUpdate
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
            serving_unit=obj_in.serving_unit,
            serving_weight_grams=obj_in.serving_weight_grams,
            food_name=obj_in.food_name,
            user_id=obj_in.user_id
        )
        db.add(food_log_obj)
        db.commit()
        db.refresh(food_log_obj)
        return food_log_obj
    

    
    def get_food_logs_for_user(self, db: Session, user_id: int):
        # Query to get all food logs for a specific user
        user_food_logs = (
            db.query(FoodLog)
            .join(UsersToFoods, UsersToFoods.food_id == FoodLog.id)
            .filter(UsersToFoods.user_id == user_id)
            .all()
        )

        return user_food_logs
    
    
flc = FoodLogController(FoodLog)