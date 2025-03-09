from datetime import datetime
from decluttr import db
from flask_login import UserMixin
from sqlalchemy import Numeric


    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Order ID 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    variant_id = db.Column(db.Integer, db.ForeignKey('product_variant.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.product_id}', '{self.quantity}', '{self.selected_size}', '{self.date_added}')"
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    order_status = db.Column (db.String(20), nullable =False)
    date_purchase = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.order_id}', '{self.product_id}', '{self.order_total}', '{self.date_purchase}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Product ID
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=True)
    condition = db.Column(db.String(100), nullable=False)
    price = db.Column(Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"