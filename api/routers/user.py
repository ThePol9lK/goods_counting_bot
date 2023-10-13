from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user as UserServices
from dto import user as UserDTO

router = APIRouter()


@router.post('/', tags=['user'])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserServices.create_user(data, db)


@router.get('/all', tags=['user'])
async def get_all(db: Session = Depends(get_db)):
    return UserServices.get_all_user(db)


@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserServices.get_user(id, db)


@router.put('/{id}', tags=['user'])
async def update(id: int = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserServices.update_user(id, data, db)


@router.delete('/{id}', tags=['user'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserServices.remove_user(id, db)
