from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps

class FoodLogController:
    def get_current_user(db: Session = Depends(deps.get_db)):
        user = deps.get_current_user(db)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        return user