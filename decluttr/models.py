from datetime import datetime
from decluttr import db
from flask_login import UserMixin
from sqlalchemy import Numeric
from decluttr import bcrypt

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_level = db.Column (db.Integer, db.ForeignKey('user_level.user_level'), default=1, nullable=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.sr_code}', '{self.program}')"

class UserLevel(db.Model):
    user_level = db.Column(db.Integer, primary_key=True)
    level_name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"UserLevel('{self.level_name}')"

 
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


class ProductVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True) ## Product Variant ID
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    color = db.Column(db.String(20), nullable=True)
    storage = db.Column(db.String(20), nullable=False)
    price = db.Column(Numeric(2), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref='variants')

    def __repr__(self):
        return f"ProductVariant('{self.product_id}', '{self.size}', '{self.stock}')"