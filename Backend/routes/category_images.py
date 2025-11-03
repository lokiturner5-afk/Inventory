from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.categoryimageschema import CategoryImageRead
import models
from typing import List


routes = APIRouter(prefix="/catigorye_images", tags=['Category Images'])

@routes.get("/images", response_model=List[CategoryImageRead])
def get_images(db:Session = Depends(get_db)):
    return db.query(models.CategoryImage).all()

@routes.delete("/remove-image/{category_image_id}")
def remove_image(category_image_id:int, db:Session = Depends(get_db)):
    data = db.query(models.CategoryImage).filter(models.CategoryImage.id == category_image_id).first()
    if not data:
        raise HTTPException(detail="data not found", status_code=404)
    
    db.delete(data)
    db.commit()
    return {"message": "Data has been removed successfully"}