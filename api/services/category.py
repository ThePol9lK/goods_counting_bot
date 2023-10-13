from models.category import Category
from sqlalchemy.orm import Session
from dto import category


def create_category(data: category.Category, db):
    category = Category(name=data.name)

    try:
        db.add(category)
        db.commit()
        db.refresh(category)

    except Exception as e:
        print(e)

    return category


def get_all_categories(db):
    return db.query(Category).all()


def update_category(id: int, data: category.Category, db: Session):
    category = db.query(Category).filter(Category.id == id).first()
    category.name = data.name
    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def remove_category(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id).delete()
    db.commit()
    return category
