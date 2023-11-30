from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
# from app.models.nutritionix_foods import Nutritionix
from app.schemas.nutritionix_foods import NutritionixSchema
from app.api import deps
from app import controllers, models, schemas
from app.db import session
from app.controllers.NutritionixController import NutritionixController



router = APIRouter()

@router.get("/list", response_model=List[NutritionixSchema])
def list_nutritionix(skip: int = 0, db: Session = Depends(deps.get_db)):
    nutritionix_controller = NutritionixController()
    nutritionix_items = nutritionix_controller.get_nutritionix_list(db=db, skip=skip)
    return nutritionix_items
