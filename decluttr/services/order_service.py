from models import db, Order

def create_order(user_id, product_id, order_quantity, order_status="Pending"):
    new_order = Order(user_id=user_id, product_id=product_id, order_quantity=order_quantity, order_status=order_status)
    db.session.add(new_order)
    db.session.commit()
    return new_order

def get_order_by_id(order_id):
    return Order.query.get(order_id)
