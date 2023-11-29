from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Nutritonix(Base):
    __tablename__ = "nutritionix_foods"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, index=True)
    name = Column(String, index=True)
    calories = Column(Float, index=True)
    servings_size = Column(Integer, index=True)