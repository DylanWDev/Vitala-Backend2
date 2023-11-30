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



@router.post("/create", response_model=NutritionixSchema)
def create_nutritionix(item: NutritionixSchema, db: Session = Depends(deps.get_db)):
    nutritionix_controller = NutritionixController()
    new_nutritionix = nutritionix_controller.create_nutritionix_item(db=db, item=item)
    return new_nutritionix



@router.delete("/delete/{id}", response_model=NutritionixSchema)
def delete_nutritionix(id: int, db: Session = Depends(deps.get_db)):
    nutritionix_controller = NutritionixController()
    item = nutritionix_controller.get_nutritionix_by_id(db=db, item_id=id)
    if item:
        delete_item = nutritionix_controller.delete_nutritionix_item(db=db, id=id)
        return delete_item
    else:
        raise HTTPException(status_code=404, detail="Item not found", headers={"Content-Type": "application/json"})