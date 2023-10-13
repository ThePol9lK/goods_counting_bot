from models.transaction import Transaction
from sqlalchemy.orm import Session
from dto import transaction


def create_transaction(data: transaction.Transaction, db):
    transaction = Transaction(id_user=data.id_user, id_product=data.id_product, description=data.description, count=data.count)

    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)

    except Exception as e:
        print(e)

    return transaction


def get_transaction(id: int, db):
    return db.query(Transaction).filter(Transaction.id == id).first()


def get_all_transaction(db):
    return db.query(Transaction).all()
