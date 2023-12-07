from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.api import deps
from app import controllers, models, schemas
from typing import Any, List

router = APIRouter()

@router.post("/", response_model=schemas.FoodLogSchema)
def create_food_log(
    *,
    food_log: schemas.FoodLogBase,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_user),
):
    result = controllers.flc.create(db, obj_in=food_log)
    return result


@router.get('/all_food_logs', response_model=List[schemas.FoodLogSchema])
def read_food_log(
        db: Session= Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    
    result = controllers.flc.get_multi(db, skip=skip, limit=limit)
    return result


@router.get("/get_my_food_logs", response_model=List[schemas.FoodLogSchema])
def get_my_food_logs(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> List[schemas.FoodLogSchema]:
    """
    Update specific information for the user without authentication.
    """
    user_food_logs = controllers.user.get_my_food_logs(db, user_id=int(user_id))
   
    if not user_food_logs:
        raise HTTPException(status_code=404, detail="FoodLogs not found for " + str(user_id))
    return user_food_logs


@router.delete("/{food_log_id}", response_model=schemas.FoodLogSchema)
def delete_food_log(
    food_log_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    result = controllers.flc.remove(db, id=food_log_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food Log with id {food_log_id} not found",
        )
    return result


@router.put("/{food_log_id}", response_model=schemas.FoodLogSchema)
def update_food_log_full(
    food_log_id: int,
    food_log_update: schemas.FoodLogSchema,
    db: Session = Depends(deps.get_db),
) -> Any:
    existing_food_log = controllers.flc.get(db, id=food_log_id)
    if existing_food_log is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food Log with id {food_log_id} not found",
        )
    
    updated_food_log = controllers.flc.update(db, db_obj=existing_food_log, obj_in=food_log_update)
    return updated_food_log



@router.patch("/{food_log_id}", response_model=schemas.FoodLogSchema)
def update_food_log_partial(
    food_log_id: int,
    column_name: str,  
    column_value: Any,  
    db: Session = Depends(deps.get_db),
) -> Any:
    existing_food_log = controllers.flc.get(db, id=food_log_id)
    if existing_food_log is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food Log with id {food_log_id} not found",
        )

    
    setattr(existing_food_log, column_name, column_value)

    db.commit()
    db.refresh(existing_food_log)

    return existing_food_log

