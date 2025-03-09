import os
from decluttr import db
from decluttr.models import Category, Product, ProductVariant

# Function to generate image URL based on product name
def generate_image_url(product_name):
    img_folder = os.path.join('static', 'img')
    img_filename = f"{product_name.lower()}.png"
    img_path = os.path.join(img_folder, img_filename)
    return img_path.replace('/', '\\')

# Create Categories
uniform_category = Category(name='Uniform')
univ_merch_category = Category(name='UnivMerch')
org_merch_category = Category(name='OrgMerch')

# Add Categories to the database
db.session.add_all([uniform_category, univ_merch_category, org_merch_category])
db.session.commit()

# Create Products for Uniform
polo = Product(name='Polo', price=12.50, category=uniform_category, image_url=generate_image_url('Polo'))
pants = Product(name='Pants', price=12.50, category=uniform_category, image_url=generate_image_url('Pants'))
blouse = Product(name='Blouse', price=12.50, category=uniform_category, image_url=generate_image_url('Blouse'))
skirt = Product(name='Skirt', price=12.50, category=uniform_category, image_url=generate_image_url('Skirt'))
pe_shirt = Product(name='PE Shirt', price=12.50, category=uniform_category, image_url=generate_image_url('PE Shirt'))
pe_pants = Product(name='PE Pants', price=12.50, category=uniform_category, image_url=generate_image_url('PE Pants'))

# Add Products to the database
db.session.add_all([polo, pants, blouse, skirt, pe_shirt, pe_pants])
db.session.commit()

# Create Products for UnivMerch
bamboo_tumbler = Product(name='Bamboo Tumbler', price=12.50, category=univ_merch_category, image_url=generate_image_url('Bamboo Tumbler'))
bsu_umbrella = Product(name='BSU Umbrella', price=12.50, category=univ_merch_category, image_url=generate_image_url('BSU Umbrella'))
shot_glass = Product(name='Shot Glass', price=12.50, category=univ_merch_category, image_url=generate_image_url('Shot Glass'))
coffee_mug = Product(name='Coffee Mug', price=12.50, category=univ_merch_category, image_url=generate_image_url('Coffee Mug'))
notepad = Product(name='Notepad', price=12.50, category=univ_merch_category, image_url=generate_image_url('Notepad'))
tote_bag = Product(name='Tote Bag', price=12.50, category=univ_merch_category, image_url=generate_image_url('Tote Bag'))


# Add Products to the database
db.session.add_all([bamboo_tumbler, bsu_umbrella, shot_glass, coffee_mug, notepad, tote_bag])
db.session.commit()

# Create Products for OrgMerch
aces_shirt = Product(name='ACES Shirt', price=12.50, category=org_merch_category, image_url=generate_image_url('ACES Shirt'))
aces_org_shirt = Product(name='ACES Org Shirt', price=12.50, category=org_merch_category, image_url=generate_image_url('ACES Org Shirt'))
cafad_shirt = Product(name='CAFAD Shirt', price=12.50, category=org_merch_category, image_url=generate_image_url('CAFAD Shirt'))
cheo_shirt = Product(name='CHEO Shirt', price=12.50, category=org_merch_category, image_url=generate_image_url('CHEO Shirt'))
cics_shirt = Product(name='CICS Shirt', price=12.50, category=org_merch_category, image_url=generate_image_url('CICS Shirt'))
bucket_hat = Product(name='Bucket Hat', price=12.50, category=org_merch_category, image_url=generate_image_url('Bucket Hat'))


# Add Products to the database
db.session.add_all([aces_shirt, aces_org_shirt, cafad_shirt, cheo_shirt, cics_shirt, bucket_hat])
db.session.commit()

# Create Product Variants for Uniform and OrgMerch
uniform_sizes = ['Extra Small', 'Small', 'Medium', 'Large', 'Extra Large']
for product in [polo, pants, blouse, skirt, pe_shirt, pe_pants]:
    for size in uniform_sizes:
        variant = ProductVariant(product=product, size=size, stock=10)  # Set stock to a random non-zero value
        db.session.add(variant)

univ_sizes = ['Single Size']
for product in [bamboo_tumbler,bsu_umbrella, shot_glass, notepad, coffee_mug, tote_bag]:
    for size in univ_sizes:
        variant = ProductVariant(product=product, size=size, stock=10)  # Set stock to a random non-zero value
        db.session.add(variant)

org_sizes = ['Extra Small', 'Small', 'Medium', 'Large', 'Extra Large']
for product in [aces_shirt, aces_org_shirt, cafad_shirt, cheo_shirt, cics_shirt, bucket_hat]:
    for size in org_sizes:
        variant = ProductVariant(product=product, size=size, stock=10)  # Set stock to a random non-zero value
        db.session.add(variant)



# Commit changes to the database
db.session.commit()
