from sqlalchemy import Column, Integer, String, Float


from app.db.base_class import Base

class Nutritionix(Base):
    __tablename__ = "nutritionix_foods"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, index=True)
    name = Column(String, index=True)
    calories = Column(Float, index=True)
    servings_size = Column(Integer, index=True)