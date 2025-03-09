<p align = "center">
  <img src = "bsu_logo.png" width = "300" height = "300" alt="LogoInsert"> 
</p>

# BatState-U Community Marketplace

<br> A proposed community marketplace for Batangas State University. A centralized shop for students' educational necessities. 
<br>

## Installation and Set-up
  &nbsp;&nbsp;&nbsp; First install the dependencies required on the requirements.txt. To do this run  the `terminal` and enter the command below.

``` powershell
    pip install -r requirements.txt
```
&nbsp;&nbsp;&nbsp; To run the program, open the `termminal` and navigate on the project directory using `cd` then run the command below.
```powershell
  python run.py
```

## Table of Contents

### [1. Objective](#obj)
### [2. Project Overview](#proj-obv) 
- #### [Object Oriented Programming Concepts](#oop)
- #### [The Database](#db)
### [3. Technical Overview](#tech-info)
### [4. Technology Stacks](#tech-stacks) 
### [6. Future](#roadm) 
### [7. Contributors](#contrib) 
### [8. Notes](#notes) 

<br><br>

## <a id = "proj-obv"> 🎯Project Overview </a> <br>
 The BatState-U Community Marketplace is a web application designed to serve as a centralized platform, while also allowing students to offer their service and product to the BatState-U community.  This marketplace aims to streamline the process of acquiring academic essentials and other services – providing a convenient and efficient solution for the BatState-U community.

 <br>

###  Project Focus:
The current focus of the platform (as of 2023) is laying the cetralized groundwork for the platform; however, upcoming updates will introduce a pivotal feature—empowering students to offer their services to the community. This enhancement will broaden the scope of the marketplace, fostering a collaborative ecosystem within the BatState-U community.

 > The feature allowing students to offer service to the community is currently unavailable and to be part of future updates . 

<br><br>




##  <a id = "obj"> 📈 Objective </a><br>


- <b> Centralized Platform</b>: Create a one-stop-shop for students to easily find and purchase educational materials within the BatState-U community. <br><br>



- <b>Efficient Procurement</b>: Simplify the process of acquiring academic necessities, reducing the time and effort students spend on searching for supplies.<br><br>


 - <b>Community Engagement</b>: Foster a sense of community by connecting students and providing a platform for interaction through buying and selling educational items. <br><br>

 
The project is aligned with the 17 Sustainable Development Goals (SDG), specifically the following:

> 8th Decent Work and Economic Growth <br>
> 9th Industry, Innovation and Infrastracture <br>
> 11th Sustainable Cities and Communities <br>

<br>

##  <a id = "tech-info"> Technical Overview</a><br>


This project is inline with the the developers' requisite in their <b>Object Oriented Programming (OOP)</b> and <b>Database Management Systems (DBMS)</b> courses .



With this, the developers are expected to apply key principles of Object-Oriented Programming to design and structure the codebase efficiently. They should demonstrate a solid understanding of concepts such as encapsulation, inheritance, and polymorphism, ensuring that the code is not only functional but also maintainable and extensible.

Below are some of the examples of the utilization of the OOP principles in the program




- #### <span style="color: black;" id="oop">Encapsulation </span>    

```python


### In file "models.py"

class User(db.Model, UserMixin):
    # Attributes (name, email, sr_code, program, password) are encapsulated within this class.

class UserLevel(db.Model):
    # Attributes (user_level, level_name) are encapsulated within this class.

class Category(db.Model):
    # Attributes (id, name) are encapsulated within this class.

class Product(db.Model):
    # Attributes (id, category_id, name, price, description, image_url) are encapsulated within this class.

class ProductVariant(db.Model):
    # Attributes (id, product_id, size, stock) are encapsulated within this class.

class Cart(db.Model):
    # Attributes (id, user_id, product_id, quantity, selected_size, date_added) are encapsulated within this class.

class Order(db.Model):
    # Attributes (id, user_id, product_id, order_quantity, order_total, order_size, date_purchase) are encapsulated within this class.

### Each class encapsulates its attributes, defining a clear boundary for the data it holds. For example, the User class encapsulates user-related attributes.

```
- #### Inheritance

```python


### In file "models.py"

class User(db.Model, UserMixin):
    # Inherits from db.Model and UserMixin

class UserLevel(db.Model):
    # Inherits from db.Model

class Category(db.Model):
    # Inherits from db.Model

class Product(db.Model):
    # Inherits from db.Model

class ProductVariant(db.Model):
    # Inherits from db.Model

class Cart(db.Model):
    # Inherits from db.Model

class Order(db.Model):
    # Inherits from db.Model

### Each class inherits from db.Model in Flask-SQLAlchemy, and User class also inherits from UserMixin for Flask-Login integration.

```
<br>

- #### Polymorphism


```python


### In file "search.js"

class Filter {
  constructor(elements) {
    this.elements = Array.from(elements);
  }

  applyFilter(searchTerm) {
    throw new Error("Subclasses must implement the applyFilter method");
  }

  addEventListeners() {
    throw new Error("Subclasses must implement the addEventListeners method");
  }
}

class ProductNameFilter extends Filter {
  constructor(searchInput, productList) {
    super(productList);
    this.searchInput = searchInput;
    this.addEventListeners();
  }

class SectionFilter extends Filter {
  constructor(element) {
    super([element]);
    this.addEventListeners();
  }

  applyFilter() {
    scrollIntoViewSmooth(this.elements[0]);
  }

  addEventListeners() {
    this.elements[0].addEventListener("click", () => {
      this.applyFilter();
    });
  }
}

ProductNameFilter and SectionFilter extend the Filter class, inheriting the common interface.They provide their implementations of the abstract methods (applyFilter and addEventListeners), demonstrating polymorphism.
```

<br>

- #### Abstraction

```python


### In file "models.py"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sr_code = db.Column(db.String(20), unique=True, nullable=False)
    program = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_level = db.Column (db.Integer, db.ForeignKey('user_level.user_level'), default=1, nullable=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.sr_code}', '{self.program}')"

    # Abstraction of a user with attributes like name, email, sr_code, program, etc.

### Encapsulating the attributes and providing a representation method, the User class abstracts the complexities of user management, providing a clean and simplified interface for working with user entities.

```
<br>





#### <span style="color: black;" id="db"> 1. Database Management System </span>
<br>
<br>


            1.1 Choice of Database System
<br>

The project utilizes SQLite as its database management system. The decision to use SQLite over MySQL was based on several factors, including:

- <b>Simplicity</b>: SQLite is a lightweight, serverless, and self-contained database engine. It does not require a separate server process and is easy to set up and manage, making it a suitable choice for smaller projects.
<br>
- <b>Portability</b>: SQLite databases are stored as a single file, making them highly portable. This simplicity is advantageous for development, testing, and deployment across different environments.

<br>
<br>


            1.2 Database Schema
            
The database schema is defined in the `models.py` file. This file contains metadata describing the structure of the database, including tables, fields, and relationships.
<br>


 
```python

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sr_code = db.Column(db.String(20), unique=True, nullable=False)
    program = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_level = db.Column (db.Integer, default=1)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.sr_code}', '{self.program}')"
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"
    

    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=True) 
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"
    

class ProductVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size = db.Column(db.String(20), nullable=True)  # Assuming size is a string
    stock = db.Column(db.Integer, nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref='variants')

    def __repr__(self):
        return f"ProductVariant('{self.product_id}', '{self.size}', '{self.stock}')"

    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    selected_size = db.Column(db.String(20), nullable=True)  # New field for selected size
    date_added = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.product_id}', '{self.quantity}', '{self.selected_size}', '{self.date_added}')"
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order_quantity = db.Column(db.Integer, nullable=True)
    order_total = db.Column(Numeric(10, 2), nullable=False) 
    order_size = db.Column(db.String(20), nullable=True)  # New field for selected size
    date_purchase = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.order_id}', '{self.product_id}', '{self.order_total}', '{self.date_purchase}')"
```


          1.3 Future Roadmap: Transition to MySQL

While SQLite is suitable for development, there is a planned transition to MySQL for the production environment. Several factors influence this decision: Scalability, Concurrency and Multi-User Support and Additional Features. 

<br>

#### 2. Querying Approach
        2.1 ORM (Object-Relational Mapping)
The project leverages an ORM for database interactions. ORM is a programming technique that allows the conversion between object-oriented programming languages and relational database management systems. 

<br>



        2.2 Raw SQL
In addition to the ORM, raw SQL queries are employed for certain database operations. This hybrid approach is chosen for specific scenarios:



   
<br>

##  <a id = "tech-stacks"> ⚙️ Technology Stack </a><br>
The following listed tools are utilized in this project. <br>

<b>Backend</b> 
- [x] Flask <br> 

<b>Database </b>
- [x] SQLite


<b>Front-End </b>

- [x] HTML/CSS <br> 
- [x] Bootstrap <br> 
- [x] Javascript <br>

<br>



In addition, the dependencies and libraries that are found in the `requirements.txt` are listed below:
- [x]   alembic==1.12.1
- [x]   bcrypt==4.0.1
- [x]   blinker==1.7.0
- [x]   click==8.1.7
- [x]   colorama==0.4.6
- [x]   dnspython==2.4.2
- [x]   email-validator==2.1.0.post1
- [x]   Flask==3.0.0
- [x]   Flask-Bcrypt==1.0.1
- [x]   Flask-Login==0.6.3
- [x]   Flask-Migrate==4.0.5
- [x]   Flask-MySQLdb==2.0.0
- [x]   Flask-SQLAlchemy==3.1.1
- [x]   Flask-WTF==1.2.1
- [x]   greenlet==3.0.1
- [x]   idna==3.4
- [x]   importlib-metadata==6.8.0
- [x]   itsdangerous==2.1.2
- [x]   Jinja2==3.1.2
- [x]   Mako==1.3.0
- [x]   MarkupSafe==2.1.3
- [x]   mysqlclient==2.2.0
- [x]   SQLAlchemy==2.0.23
- [x]   typing_extensions==4.8.0
- [x]   Werkzeug==3.0.1
- [x]   WTForms==3.1.1
- [x]   zipp==3.17.0
<br>

##  <a id = "roadm"> 🛣️ Future</a> <br>


##### 1. Payment System Integration
<br>

- To enhance the user experience, the future development of the BatState-U Community Marketplace will include the integration of a secure and user-friendly payment system. This will allow users to seamlessly conduct transactions within the platform, providing a convenient way to purchase educational necessities and other services.
<br>

##### 2. Migration to a Production Database
<br>

- As the platform evolves, there will be a transition from the current development database to a robust production database. This migration aims to optimize data storage, retrieval, and overall system performance, ensuring a smooth and reliable experience for users.
<br>

<br>

##### 3. Enhanced Security Features
<br>

- To prioritize the safety and privacy of users, the future releases of the marketplace will implement advanced security measures. This includes encryption protocols, secure authentication processes, and regular security audits to identify and address potential vulnerabilities.
<br>



##### 4. App Policy Implementation
<br>

- A comprehensive set of policies governing products, ordering processes, and payments will be established. These policies will ensure a fair, transparent, and secure environment for both buyers and sellers. Users will be provided with clear guidelines, contributing to a positive and trustworthy community marketplace.


<br>


##### 5. Improved Scalability Across Different End-Devices


<br>


- To cater to the diverse needs of the BatState-U community, the marketplace will undergo optimizations for improved scalability. This includes responsive design elements and performance enhancements to ensure a seamless experience across various devices such as desktops, tablets, and smartphones.

<br>

##### 6. Buyer and Seller Interaction Features

<br>


- The future iterations of the BatState-U Community Marketplace will introduce features that facilitate communication between buyers and sellers. This may include chat functionality, order status updates, and a rating system to build a sense of community and trust among users.

<br>


##### 7. Enhanced UI Design

<br>


- Aesthetics and usability play a crucial role in user satisfaction. The marketplace will undergo a UI (User Interface) overhaul to provide an intuitive, visually appealing, and user-friendly interface. This enhancement aims to make navigation and interaction more engaging and enjoyable for the BatState-U community.
<br>

<br>


##  <a id = "contrib"> 👷‍ Contributors </a> <br>

| Name | Role | E-mail | Other Contacts |
| --- | --- | --- | --- |
| <a href = "https://github.com/DirkSteven">Dirk Steven E. Javier</a> | x | dirkjaviermvp@gmail.com |
| <a href = "https://x">x </a>|  Developer  | x |
| <a href = "https:/x">x </a>| Developer | x |



<br>


##  <a id = "notes"> 📝 Notes </a><br>
<!-- [1] *** INSERT NOTE ***

[2] *** INSERT NOTE *** -->

<br><br>



