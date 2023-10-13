from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import category as CategoryServices
from dto import category as CategoryDTO

router = APIRouter()


@router.post('/', tags=['category'])
async def create(data: CategoryDTO.Category = None, db: Session = Depends(get_db)):
    return CategoryServices.create_category(data, db)


@router.get('/all', tags=['category'])
async def get(db: Session = Depends(get_db)):
    return CategoryServices.get_all_categories(db)


@router.put('/{id}', tags=['category'])
async def update(id: int = None, data: CategoryDTO.Category = None, db: Session = Depends(get_db)):
    return CategoryServices.update_category(id, data, db)


@router.delete('/{id}', tags=['category'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return CategoryServices.remove_category(id, db)
