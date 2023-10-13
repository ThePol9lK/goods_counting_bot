from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import transaction as TransactionServices
from dto import transaction as TransactionDTO

router = APIRouter()


@router.post('/', tags=['transaction'])
async def create(data: TransactionDTO.Transaction = None, db: Session = Depends(get_db)):
    return TransactionServices.create_transaction(data, db)


@router.get('/{id}', tags=['transaction'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return TransactionServices.get_transaction(id, db)


@router.get('/all', tags=['transaction'])
async def get(db: Session = Depends(get_db)):
    return TransactionServices.get_all_transaction(db)
