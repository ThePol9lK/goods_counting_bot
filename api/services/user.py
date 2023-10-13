from models.user import User
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db):
    user = User(name=data.name, id_telegram=data.id_telegram, admin=data.admin)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    except Exception as e:
        print(e)

    return user


def get_user(id: int, db):
    return db.query(User).filter(User.id == id).first()


def get_all_user(db):
    return db.query(User).all()


def update_user(id: int, data: user.User, db: Session):
    user = db.query(User).filter(User.id == id).first()
    user.name, user.id_telegram, user.admin = data.name, data.id_telegram, data.admin
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def remove_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user
