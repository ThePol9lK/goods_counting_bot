from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import product as ProductServices
from dto import product as ProductDTO

router = APIRouter()


@router.post('/', tags=['product'])
async def create(data: ProductDTO.Product = None, db: Session = Depends(get_db)):
    return ProductServices.create_product(data, db)


@router.get('/all', tags=['product'])
async def get(db: Session = Depends(get_db)):
    return ProductServices.get_all_products(db)


@router.get('/{id}', tags=['product'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return ProductServices.get_product(id, db)


@router.put('/{id}', tags=['product'])
async def update(id: int = None, data: ProductDTO.Product = None, db: Session = Depends(get_db)):
    return ProductServices.update_product(id, data, db)


@router.delete('/{id}', tags=['product'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return ProductServices.remove_product(id, db)
