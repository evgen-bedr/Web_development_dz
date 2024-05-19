from dz_web_development.dz_4.connector import DBConnector
from dz_web_development.dz_4 import engine
from dz_web_development.dz_4.models import Category, Product
from sqlalchemy import func

with DBConnector(engine=engine) as session:
    # Задача 2: Чтение данных
    # Извлеките все записи из таблицы categories.
    # Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.
    # ==================================================================================================
    print(2, "=" * 100)

    all_shortcuts = session.query(Category).all()

    for cat in all_shortcuts:
        print()
        print(f"{'=' * (len(cat.name) + 4)}")
        print(f"= {cat.name} =")
        print(f"{'=' * (len(cat.name) + 4)}")

        for product in cat.products:
            print(f"{product.name} | Price: {product.price} | Available: {product.available}")

    print()
    print(3, "=" * 100)
    print()

    # Задача 3: Обновление данных
    # Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
    # ==================================================================================================

    smartphone: Product = session.query(Product).filter(Product.name == 'Смартфон').first()
    if smartphone:
        smartphone.price = 349.99
        session.commit()

    print(smartphone.name, smartphone.price)
    print()
    print(4, "=" * 100)
    print()

    # Задача 4: Агрегация и группировка
    # Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
    # ==================================================================================================

    count_items_by_category = session.query(
        Category.name, func.count(Product.id).label('product_count')
    ).join(Product).group_by(Category.id).all()

    for category_name, product_count in count_items_by_category:
        print(f"{category_name}, Number of Products: {product_count}")

    print()
    print(5, "=" * 100)
    print()

    # Задача 5: Группировка с фильтрацией
    # Отфильтруйте и выведите только те категории, в которых более одного продукта.
    # ==================================================================================================

    # cat_more_then_one = session.query(
    #     Category.name, func.count(Product.id).label('product_count')
    # ).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()

    product_count = func.count(Product.id).label('product_count')

    cat_more_than_one = session.query(
        Category.name, product_count
    ).join(Product).group_by(Category.id).having(product_count > 1).all()

    for category_name, count in cat_more_than_one:
        print(f"{category_name}, Number of Products: {count}")
