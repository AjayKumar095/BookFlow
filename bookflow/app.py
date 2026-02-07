from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
from config import Config
from models import db, Author, Book, Sale, Withdrawal

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Enable CORS for all routes
db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to BookFlow!'


@app.route('/authors', methods=["GET"])
def get_authors():
    authors = Author.query.all()
    authors_data = []
    
    for author in authors:
        books = Book.query.filter_by(author_id=author.id).all()
        
        total_earnings = 0
        for book in books:
            sales = Sale.query.filter_by(book_id=book.id).all()
            sold = sum(sale.quantity for sale in sales)
            total_earnings += sold * book.royalty_per_sale
        
        withdrawals = Withdrawal.query.filter_by(author_id=author.id).all()
        withdrawn_amount = sum(withdrawal.amount for withdrawal in withdrawals)
        current_balance = total_earnings - withdrawn_amount
        
        authors_data.append({
            "id": author.id,
            "name": author.name,
            "total_earnings": total_earnings,
            "current_balance": current_balance
        })
    
    return jsonify(authors_data), 200    

@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_details(author_id):
    try:
        author = Author.query.get_or_404(author_id)
        books = Book.query.filter_by(author_id=author_id).all()
        books_data = []
       
        total_earnings = 0
        for book in books:
           sales = Sale.query.filter_by(book_id=book.id).all()
           sold = sum(sale.quantity for sale in sales)
           total_earnings += sold * book.royalty_per_sale
           
           books_data.append({
               "id": book.id,
               "title": book.title,
               "royalty_per_sale": book.royalty_per_sale,
               "total_sold": sold,
               "total_royalty": sold * book.royalty_per_sale
                
                })
        
        withdrawals = Withdrawal.query.filter_by(author_id=author_id).all()
        withdrawn_amount = sum(withdrawal.amount for withdrawal in withdrawals)
        current_balance = total_earnings - withdrawn_amount
           
           
        
        return jsonify({
            "id": author.id,
            "name": author.name,
            "email": author.email, 
            "total_earnings": total_earnings,
            "current_balance": current_balance,
            "total_books": len(books),
            "books": books_data
        }), 200
    
    except Exception:
        return jsonify({"error": str("404 Not Found")}), 404  

@app.route('/authors/<int:author_id>/sales', methods=["GET"])
def get_author_sales(author_id):
    try:
        author = Author.query.get_or_404(author_id)
        books = Book.query.filter_by(author_id=author_id).all()
        sales_data = []
        
        for book in books:
            sales = Sale.query.filter_by(book_id=book.id).all()
            for sale in sales:
                sales_data.append({
                    "book_title": book.title,
                    "quantity": sale.quantity,
                    "sale_date": sale.sale_date,
                    "royalty_earned": sale.quantity * book.royalty_per_sale
                })
        
        sales_data.sort(key=lambda x: x["sale_date"], reverse=True)
        return jsonify(sales_data), 200        
        
    
    except Exception:
        return jsonify({"error": str("404 Not Found")}), 404  
            

if __name__ == '__main__':
    app.run(debug=True)