from sqlalchemy import Column, Integer, ForeignKey, Text
from database import Base


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_product = Column(Integer, ForeignKey('product.id'))
    description = Column(Text, index=True)
    count = Column(Integer, index=True)
