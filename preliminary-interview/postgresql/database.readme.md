####################### PostreSQL Database

### database editor playground:

https://pg-sql.com/

### creating or designing database:

the process of designing database is creating table,creating columns, and setting the columns data type.
 

### creating database with SQL query:

CREATE TABLE countries(
  name VARCHAR(40),
  population INTEGER,
  area INTEGER
  );


### inserting into a table with SQL query:

INSERT INTO countries(name,population,area)
VALUES('Indonesia',270000000,25000000)

### setting foreign key 

CREATE TABLE production (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  amount INTEGER,
  country_id INTEGER REFERENCES countries(id)
  );


### simple database schema :
-- Table for departments
CREATE TABLE departments (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50)
);

-- Table for employees
CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  department_id INTEGER REFERENCES departments(id)
);

### Design a Library system schema

# Django

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField()



### Sketch Schema

library_book: id, title, author
library_member: id, name, email
library_loan: id, book_id -> library_book(id), member_id -> library_member(id), loan_date


### Model an E-commerce System

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped')], default='pending')

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])


### Sketch Schema 

ecommerce_product: id, name, price
ecommerce_customer: id, name, email
ecommerce_order: id, customer_id -> ecommerce_customer(id), order_date, status
ecommerce_order_line: id, order_id -> ecommerce_order(id), product_id -> ecommerce_product(id), quantity

### queries 
SELECT c.name AS customer_name, p.name AS product_name, ol.quantity, p.price * ol.quantity AS line_total
FROM ecommerce_order_line ol
JOIN ecommerce_order o ON ol.order_id = o.id
JOIN ecommerce_customer c ON o.customer_id = c.id
JOIN ecommerce_product p ON ol.product_id = p.id
WHERE o.status = 'pending';


SELECT c.name, c.email, COUNT(o.id) AS order_count, SUM(p.price * ol.quantity) AS total_spent
FROM ecommerce_order_line ol
JOIN ecommerce_order o ON ol.order_id = o.id
JOIN ecommerce_customer c ON o.customer_id = c.id
JOIN ecommerce_product p ON ol.product_id = p.id
GROUP BY c.id, c.name, c.email;