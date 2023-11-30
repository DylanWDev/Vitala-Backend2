from sqlalchemy.orm import Session
from app.models.nutritionix_foods import Nutritionix
from app.schemas.nutritionix_foods import NutritionixSchema

class NutritionixController:
    def get_nutritionix_list(self, db: Session, skip: int = 0) -> list[Nutritionix]:
        items = db.query(Nutritionix).offset(skip).all()
        return items

    def get_nutritionix_by_id(self, db: Session, item_id: int) -> Nutritionix:
        item = db.query(Nutritionix).filter(Nutritionix.id == item_id).first()
        return item

    def create_nutritionix_item(self, db: Session, item: NutritionixSchema) -> Nutritionix:
        nutritionix = Nutritionix(**item.dict())
        db.add(nutritionix)
        db.commit()
        db.refresh(nutritionix)
        return nutritionix

    def update_nutritionix_item(self, db: Session, id: int, external_id: str, name: str, calories: str, serving_size: int) -> Nutritionix:
        item = self.get_nutritionix_by_id(db=db, item_id=id)
        item.external_id = external_id
        item.name = name
        item.calories = calories
        item.serving_size = serving_size
        db.commit()
        db.refresh(item)
        return item

    def delete_nutritionix_item(self, db: Session, id: int) -> None:
        item = self.get_nutritionix_by_id(db=db, item_id=id)
        db.delete(item)
        db.commit()
        

nutritionix_controller = NutritionixController()
