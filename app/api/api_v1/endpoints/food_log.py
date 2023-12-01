from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.controllers import FoodLogController
from app.models import FoodLog
from app.schemas.food_log import FoodLogSchema
from app.models.user import User
from app.api import deps
from app.api.deps import get_current_user


router = APIRouter()


@router.post("/foodlog", response_model=FoodLogSchema)
def create_food_log(
    food_log: FoodLogSchema,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(get_current_user),
):
    return FoodLogController.create_food_log(db, food_log, current_user.id)
