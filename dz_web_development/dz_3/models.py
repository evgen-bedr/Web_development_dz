from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey
from engine import Base, engine


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(DECIMAL(6, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))


Base.metadata.create_all(engine)
