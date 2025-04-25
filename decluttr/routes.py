from flask import render_template, url_for, flash, redirect, request, session
from flask_login import current_user, login_user, logout_user, login_required
from decluttr import app, bcrypt
from decluttr.models import Product, User, Cart, ProductVariant

@app.route('/')
@app.route('/index')
def index():
    products = Product.query.all()
    return render_template('explore.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Check if the user is logged in
    if not current_user.is_authenticated:
        flash("You must be logged in to add items to the cart.", "error")
        return redirect(url_for('login'))  # Redirect to login page if not logged in

    # If logged in, proceed with adding the item to the cart
    flash("Product added to cart!", "success")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists in the database
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # User found and password matches
            login_user(user)  # Log in the user
            flash("Login successful!", "success")  # Flash success message
            return redirect(url_for('index'))  # Redirect to explore page
        else:
            # Invalid login attempt
            flash("Login failed. Check your email and/or password.", "error")  # Flash error message
            return redirect(url_for('login'))  # Stay on the login page if authentication fails

    return render_template('login.html')



@app.route('/cart')
@login_required  # Ensure the user is logged in
def cart():
    # Retrieve the cart items for the logged-in user
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    
    # Retrieve the products and their variants for each cart item
    items = []
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        variant = ProductVariant.query.get(cart_item.variant_id)
        items.append({
            'product': product,
            'variant': variant,
            'quantity': cart_item.quantity,
            'total_price': variant.price * cart_item.quantity
        })
    
    # Calculate the overall total price
    overall_total = sum(item['total_price'] for item in items)
    
    return render_template('cart.html', items=items, overall_total=overall_total)



@app.route('/frame')
def frame():
    return render_template('frame4.html')



@app.route('/register', methods=['GET', 'POST'])
def register():

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():

    
    return render_template('forgot_password.html')

@app.route('/login/github')
def github_login():
    # In a real application, you would implement GitHub OAuth here
    # For now, we'll just redirect back to the login page with a message
    flash('GitHub login is not implemented in this demo.', 'error')
    return redirect(url_for('login'))


