from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    count = Column(Integer, index=True)
    description = Column(Text, index=True)
    image = Column(String, index=True)
    id_category = Column(Integer, ForeignKey('category.id'))
