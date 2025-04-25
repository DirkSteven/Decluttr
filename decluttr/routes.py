from flask import render_template, url_for, flash, redirect, request, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from decluttr import app, bcrypt, db
from decluttr.models import Product, User, Cart, ProductVariant
from datetime import datetime
import time
import sqlite3
import json

@app.route('/')
@app.route('/index')
def index():
    products = Product.query.all()
    product_variants = {product.id: ProductVariant.query.filter_by(product_id=product.id).all() for product in products}
    
    # Convert prices to float for template rendering
    for product in products:
        product.price = float(product.price)
    for product_id, variants in product_variants.items():
        for variant in variants:
            variant.price = float(variant.price)
    
    # Calculate cart item count for the current user
    cart_count = 0
    if current_user.is_authenticated:
        cart_count = Cart.query.filter_by(user_id=current_user.id).count()
    
    return render_template('explore.html', products=products, product_variants=product_variants, cart_count=cart_count)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    
    # Fetch all products
    products = Product.query.all()
    product_variants = {product.id: ProductVariant.query.filter_by(product_id=product.id).all() for product in products}
    
    # Filter products by name only
    query_lower = query.lower()
    filtered_products = [
        product for product in products
        if query_lower in product.name.lower() or not query_lower
    ]
    
    # Convert products and variants to JSON-serializable format
    products_json = [{
        'id': product.id,
        'name': product.name,
        'price': float(product.price),
        'image_url': product.image_url
    } for product in filtered_products]
    
    product_variants_json = {}
    for product_id, variants in product_variants.items():
        product_variants_json[product_id] = [{
            'id': variant.id,
            'color': variant.color,
            'storage': variant.storage,
            'price': float(variant.price)
        } for variant in variants]
    
    return jsonify({
        'products': products_json,
        'product_variants': product_variants_json
    })

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    max_retries = 5
    retry_delay = 1  # Delay in seconds between retries

    for attempt in range(max_retries):
        try:
            variant_id = request.form.get('variant_id')
            quantity = int(request.form.get('quantity', 1))
            product = Product.query.get_or_404(product_id)
            
            if variant_id:
                variant = ProductVariant.query.get_or_404(variant_id)
                cart_item = Cart(
                    user_id=current_user.id,
                    product_id=product.id,
                    variant_id=variant.id,
                    quantity=quantity,
                    date_added=datetime.utcnow()
                )
                flash_message = f'{product.name} ({variant.color}, {variant.storage}) added to cart!'
            else:
                cart_item = Cart(
                    user_id=current_user.id,
                    product_id=product.id,
                    variant_id=None,
                    quantity=quantity,
                    date_added=datetime.utcnow()
                )
                flash_message = f'{product.name} added to cart!'
            
            db.session.add(cart_item)
            db.session.commit()
            flash(flash_message, 'success')
            return redirect(url_for('index'))
        
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e) and attempt < max_retries - 1:
                print(f"Database locked, retrying ({attempt + 1}/{max_retries})...")
                time.sleep(retry_delay)
                db.session.rollback()
                continue
            else:
                db.session.rollback()
                flash(f'Error adding to cart: {str(e)}', 'danger')
                print(f"Error in add_to_cart: {str(e)}")
                return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding to cart: {str(e)}', 'danger')
            print(f"Error in add_to_cart: {str(e)}")
            return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/frame')
def frame():
    # Get the product_id from the query parameters
    product_id = request.args.get('product_id', type=int)
    if not product_id:
        flash('No product specified.', 'danger')
        return redirect(url_for('index'))
    
    # Fetch the product and its variants
    product = Product.query.get_or_404(product_id)
    variants = ProductVariant.query.filter_by(product_id=product.id).all()
    
    # Convert Decimal price to float for the template
    product.price = float(product.price)
    for variant in variants:
        variant.price = float(variant.price)
    
    # Calculate cart item count for the current user
    cart_count = 0
    if current_user.is_authenticated:
        cart_count = Cart.query.filter_by(user_id=current_user.id).count()
    
    return render_template('frame4.html', product=product, variants=variants, cart_count=cart_count)

@app.route('/cart')
@login_required
def cart():
    # Retrieve the cart items for the logged-in user
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    
    # Consolidate items by product_id and variant_id
    consolidated_items = {}
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        variant = ProductVariant.query.get(cart_item.variant_id) if cart_item.variant_id else None
        key = (cart_item.product_id, cart_item.variant_id)
        
        if key in consolidated_items:
            consolidated_items[key]['quantity'] += cart_item.quantity
            consolidated_items[key]['total_price'] = consolidated_items[key]['quantity'] * (float(variant.price) if variant else float(product.price))
        else:
            consolidated_items[key] = {
                'product': product,
                'variant': variant or {'color': 'N/A', 'storage': 'N/A'},
                'quantity': cart_item.quantity,
                'total_price': cart_item.quantity * (float(variant.price) if variant else float(product.price))
            }
    
    items = list(consolidated_items.values())
    
    # Calculate the overall total price
    overall_total = sum(item['total_price'] for item in items)
    
    # Calculate cart item count for the current user
    cart_count = len(cart_items)
    
    return render_template('cart.html', items=items, overall_total=overall_total, cart_count=cart_count)

@app.route('/update_quantity/<int:product_id>/<int:variant_id>', methods=['POST'])
@login_required
def update_quantity(product_id, variant_id):
    action = request.form.get('action')
    variant_id = variant_id if variant_id != 0 else None
    
    cart_items = Cart.query.filter_by(
        user_id=current_user.id,
        product_id=product_id,
        variant_id=variant_id
    ).order_by(Cart.date_added).all()
    
    if not cart_items:
        flash('Item not found in cart.', 'danger')
        return redirect(url_for('cart'))
    
    try:
        if action == 'increase':
            new_item = Cart(
                user_id=current_user.id,
                product_id=product_id,
                variant_id=variant_id,
                quantity=1,
                date_added=datetime.utcnow()
            )
            db.session.add(new_item)
            flash('Quantity increased!', 'success')
        elif action == 'decrease':
            item_to_update = cart_items[0]
            if item_to_update.quantity > 1:
                item_to_update.quantity -= 1
                flash('Quantity decreased!', 'success')
            else:
                db.session.delete(item_to_update)
                flash('Item removed from cart.', 'success')
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating cart: {str(e)}', 'danger')
    
    return redirect(url_for('cart'))

@app.route('/remove_item/<int:product_id>/<int:variant_id>', methods=['POST'])
@login_required
def remove_item(product_id, variant_id):
    cart_items = Cart.query.filter_by(user_id=current_user.id, product_id=product_id, variant_id=variant_id).all()
    
    if not cart_items:
        flash('Item not found in cart.', 'danger')
        return redirect(url_for('cart'))
    
    try:
        for item in cart_items:
            db.session.delete(item)
        db.session.commit()
        flash('Item removed from cart.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error removing item: {str(e)}', 'danger')
        print(f"Error in remove_item: {str(e)}")
    
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    selected_items = request.form.getlist('selected_items')  # Get list of selected items
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    
    # Process selected items
    checked_out_items = []
    total_amount = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        variant = ProductVariant.query.get(item.variant_id) if item.variant_id else None
        key = f"{item.product_id}_{item.variant_id or 0}"
        if key in selected_items:
            price = float(variant.price) if variant else float(product.price)
            total_price = price * item.quantity
            checked_out_items.append({
                'name': product.name,
                'variant': f"{variant.color} - {variant.storage}" if variant else "N/A",
                'quantity': item.quantity,
                'total_price': total_price
            })
            total_amount += total_price
            db.session.delete(item)
    
    if not checked_out_items:
        flash('No items were selected for checkout.', 'danger')
        return redirect(url_for('cart'))
    
    try:
        db.session.commit()
        # Store order details in session to display in dialog
        session['order_details'] = {
            'items': checked_out_items,
            'total_amount': total_amount
        }
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error during checkout: {str(e)}', 'danger')
        print(f"Error in checkout: {str(e)}")
        return redirect(url_for('cart'))

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate passwords match
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        # Combine names
        full_name = f"{first_name} {last_name}"

        # Check if email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already registered!', 'error')
            return redirect(url_for('register'))

        # Check if name already exists
        existing_name = User.query.filter_by(name=full_name).first()
        if existing_name:
            flash('Name is already taken! Please choose a different name.', 'error')
            return redirect(url_for('register'))

        try:
            # Hash password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Create new user with level 2
            new_user = User(
                name=full_name,
                email=email,
                password=hashed_password,
                user_level=2  # Set default user level to 2
            )

            # Add to database
            db.session.add(new_user)
            db.session.commit()

            # Log the user in
            login_user(new_user)
            flash('Registration successful!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            db.session.rollback()
            # More specific error message for unique constraint failures
            if "UNIQUE constraint failed: user.name" in str(e):
                flash('Name is already taken! Please choose a different name.', 'error')
            else:
                flash(f'Registration failed: {str(e)}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/login/github')
def github_login():
    # In a real application, you would implement GitHub OAuth here
    # For now, we'll just redirect back to the login page with a message
    flash('GitHub login is not implemented in this demo.', 'error')
    return redirect(url_for('login'))