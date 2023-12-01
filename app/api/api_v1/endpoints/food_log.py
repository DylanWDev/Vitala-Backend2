from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.api import deps
from app.api.deps import get_current_user
from app import controllers, models, schemas

router = APIRouter()


@router.post("/foodlog", response_model=schemas.FoodLogSchema)
def create_food_log(
    food_log: schemas.FoodLogSchema,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(get_current_user),
):
    result = controllers.flc.create_food_log(db, obj_in=schemas.FoodLogSchema)
    return result
