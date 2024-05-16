import logging
from engine import engine
from sqlalchemy.orm import sessionmaker
from models import Product, Category

logging.basicConfig(level=logging.INFO)

Session = sessionmaker(bind=engine)
session = Session()

category_1 = Category(
    name="Alcohol",
    description="Beverages containing ethanol, commonly known as alcohol. Includes a variety of drinks such as beer, wine, spirits, and liquors, each with unique flavors and characteristics. Suitable for consumption by adults, typically in social settings or special occasions."

)

category_2 = Category(
    name="Food",
    description="SOme description"

)

product_1 = Product(
    name="Beer",
    price=5.10,
    in_stock=True,
    category_id=1
)

product_2 = Product(
    name="Meat",
    price=15.50,
    in_stock=True,
    category_id=2
)

session.add(category_1)
session.add(category_2)
session.add(product_1)
session.add(product_2)

session.commit()
session.close()
