from sqlalchemy.orm import sessionmaker
from dz_web_development.dz_4 import engine
from models import Category, Product

Session = sessionmaker(bind=engine)
session = Session()

categories = [
    Category(name='Электроника', description='Гаджеты и устройства.'),
    Category(name='Книги', description='Печатные книги и электронные книги.'),
    Category(name='Одежда', description='Одежда для мужчин и женщин.')
]

session.add_all(categories)
session.commit()

electronics_id = session.query(Category.id).filter_by(name='Электроника').scalar()
books_id = session.query(Category.id).filter_by(name='Книги').scalar()
clothing_id = session.query(Category.id).filter_by(name='Одежда').scalar()

products = [
    Product(name='Смартфон', price=299.99, available=True, category_id=electronics_id),
    Product(name='Ноутбук', price=499.99, available=True, category_id=electronics_id),
    Product(name='Научно-фантастический роман', price=15.99, available=True, category_id=books_id),
    Product(name='Джинсы', price=40.50, available=True, category_id=clothing_id),
    Product(name='Футболка', price=20.00, available=True, category_id=clothing_id)
]

session.add_all(products)
session.commit()
