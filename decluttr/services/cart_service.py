from models import db, Cart

def add_to_cart(user_id, product_id, variant_id, quantity):
    cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id, variant_id=variant_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=user_id, product_id=product_id, variant_id=variant_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()

def remove_from_cart(cart_id):
    cart_item = Cart.query.get(cart_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
