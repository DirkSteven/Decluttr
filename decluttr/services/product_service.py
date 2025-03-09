from models import db, Product

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(name, brand, model, condition, price, description, image_url=None):
    new_product = Product(name=name, brand=brand, model=model, condition=condition, price=price, description=description, image_url=image_url)
    db.session.add(new_product)
    db.session.commit()
    return new_product
