from models.product import Product
from sqlalchemy.orm import Session
from dto import product


def create_product(data: product.Product, db):
    product = Product(name=data.name, count=data.count, description=data.description, image=data.image,
                      id_category=data.id_category)

    try:
        db.add(product)
        db.commit()
        db.refresh(product)

    except Exception as e:
        print(e)

    return product


def get_product(id: int, db):
    return db.query(Product).filter(Product.id == id).first()


def get_all_products(db):
    return db.query(Product).all()


def update_product(id: int, data: product.Product, db: Session):
    product = db.query(Product).filter(Product.id == id).first()
    product.name, product.count, product.description, product.image, product.id_category = data.name, data.count, data.description, data.image, data.id_category
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def remove_product(id: int, db: Session):
    product = db.query(Product).filter(Product.id == id).delete()
    db.commit()
    return product
