from flask_sqlalchemy import SQLAlchemy

## Object Relational Mapping (ORM) for database interactions
db = SQLAlchemy()

# ---------------------------------------------------------
# Required Models for BookFlow
# ---------------------------------------------------------


## Author model
class Author(db.Model):
    
    __tablename__ = "authors" # Define the table name for the Author model
    
    ## Required fields for the Author model
    
    id = db.Column(db.Integer, primary_key=True) # Primary key
    name = db.Column(db.String(100), nullable=False) # Name of the author
    email = db.Column(db.String(254), nullable=False) # Email of the author
    bank = db.Column(db.String(20), nullable=False) # Bank name for payments
    ifsc = db.Column(db.String(11), nullable=False) # IFSC code for payments
    
    book = db.relationship('Book', backref='author', lazy=True) # Relationship to the Book model
    withdrawal = db.relationship('Withdrawal', backref='author', lazy=True) # Relationship to the Withdrawal model


## Book Model
class Book(db.Model):
    
    __tablename__= "books" # Define the table name for the Book model
    
    ## Required fields for the Book model

    id = db.Column(db.Integer, primary_key=True) # Primary key
    title = db.Column(db.String(200), nullable=False) # Title of the book
    royalty_per_sale = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False) # Foreign key to the Author model
    sales = db.relationship('Sale', backref='book', lazy=True) # Relationship to the Sale model
    

## Sale Model
class Sale(db.Model):
    __tablename__ = "sales" # Table name for the sale model

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False) # book id
 
    quantity = db.Column(db.Integer, nullable=False) # Quantity of books sold
    sale_date = db.Column(db.String(20), nullable=False) # sale date of the book


## Withdrawal Model
class Withdrawal(db.Model):
    __tablename__ = "withdrawals" # Table name for the withdrawal model

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False) # Author ID

    amount = db.Column(db.Integer, nullable=False)  # Earning amount
    status = db.Column(db.String(20), default="pending") # status of withdrawal request
    created_at = db.Column(db.String(30), nullable=False)  # time of request