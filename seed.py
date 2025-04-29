from decluttr import db, app, bcrypt
from decluttr.models import User, UserLevel, Product, ProductVariant, Cart, Order
from datetime import datetime

with app.app_context():
    # Reset DB
    db.drop_all()
    db.create_all()

    # User levels
    admin_level = UserLevel(user_level=1, level_name='Admin')
    customer_level = UserLevel(user_level=2, level_name='Customer')
    db.session.add_all([admin_level, customer_level])
    db.session.commit()

    # Users
    users = [
        User(name='admin', email='admin@decluttr.com',
             password=bcrypt.generate_password_hash('adminpass').decode('utf-8'), user_level=1),
        User(name='johndoe', email='john@example.com',
             password=bcrypt.generate_password_hash('password123').decode('utf-8'), user_level=2),
        User(name='janedoe', email='jane@example.com',
             password=bcrypt.generate_password_hash('password123').decode('utf-8'), user_level=2)
    ]
    db.session.add_all(users)
    db.session.commit()

    # Products
    products = [
        Product(name="iPhone 13", brand="Apple", model="A2482", condition="Refurbished - Like New",
                price=649.99, description="Near-perfect condition iPhone 13.", image_url="/static/img/i11.jpg"),
        Product(name="iPhone 12", brand="Apple", model="A2172", condition="Refurbished - Good",
                price=499.99, description="Fully functional iPhone 12 with light wear.", image_url="/static/img/i12.jpg"),
        Product(name="iPhone 11", brand="Apple", model="A2111", condition="Refurbished - Very Good",
                price=399.99, description="Great condition iPhone 11. Battery 90%+.", image_url="/static/img/i13.jpg"),
        Product(name="iPhone XR", brand="Apple", model="A1984", condition="Refurbished - Good",
                price=299.99, description="iPhone XR with minimal signs of use.", image_url="/static/img/i14.jpg"),
        Product(name="iPhone SE (2020)", brand="Apple", model="A2275", condition="Refurbished - Very Good",
                price=279.99, description="Compact and fast SE 2nd Gen.", image_url="/static/img/i15.jpg"),
        Product(name="iPhone 13 Mini", brand="Apple", model="A2481", condition="Refurbished - Excellent",
                price=599.99, description="Small but powerful. Great battery.", image_url="/static/img/i16.jpg"),
        Product(name="iPhone 12 Pro", brand="Apple", model="A2341", condition="Refurbished - Good",
                price=729.99, description="Triple camera, great for photos.", image_url="/static/img/i17.jpg"),
        Product(name="iPhone 11 Pro Max", brand="Apple", model="A2161", condition="Refurbished - Fair",
                price=649.99, description="Large display, lots of storage.", image_url="/static/img/i18.jpg"),
    ]
    db.session.add_all(products)
    db.session.commit()

    # Variants (some phones have multiple options)
    variants = [
        ProductVariant(product_id=products[0].id, color="Red", storage="128GB", price=649.99),
        ProductVariant(product_id=products[1].id, color="Blue", storage="64GB", price=499.99),
        ProductVariant(product_id=products[1].id, color="Black", storage="128GB", price=529.99),
        ProductVariant(product_id=products[2].id, color="White", storage="64GB", price=399.99),
        ProductVariant(product_id=products[3].id, color="Coral", storage="64GB", price=299.99),
        ProductVariant(product_id=products[4].id, color="Black", storage="64GB", price=279.99),
        ProductVariant(product_id=products[5].id, color="Green", storage="128GB", price=599.99),
        ProductVariant(product_id=products[6].id, color="Pacific Blue", storage="256GB", price=729.99),
        ProductVariant(product_id=products[7].id, color="Gold", storage="512GB", price=649.99)
    ]
    db.session.add_all(variants)
    db.session.commit()

    # Cart for John
    cart_item = Cart(
        user_id=users[1].id,
        product_id=products[0].id,
        variant_id=variants[0].id,
        quantity=1
    )
    db.session.add(cart_item)

    # Order for Jane
    order = Order(
        user_id=users[2].id,
        product_id=products[2].id,
        order_quantity=1,
        order_status="Delivered",
        date_purchase=datetime.utcnow()
    )
    db.session.add(order)

    db.session.commit()
    print("Database seeded with 3 users and 8 iPhones successfully!")
