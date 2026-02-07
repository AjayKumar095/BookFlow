from app import app 
from models import db, Author, Book, Sale, Withdrawal

with app.app_context():
    
    
    ## Add authors
    author1 = Author(
        name="Priya Sharma",
        email= "priya@email.com",
        bank = "1234567890",
        ifsc = "HDFC0001234"
        
    )
    
    author2 = Author(
        name = "Rahul Verma",
        email= "rahul@email.com",
        bank = "0987654321",
        ifsc = "ICIC0005678"
    )
    
    author3 = Author(
        name="Anita Desai",
        email="anita@email.com",
        bank="5678901234",
        ifsc="SBIN0009012"
    )
    
    db.session.add_all([author1, author2, author3])
    db.session.commit()
    
    ## Add books
    book1 = Book(title="The Silent River", royalty_per_sale=45, author_id=author1.id)
    book2 = Book(title="Midnight in Mumbai", royalty_per_sale=60, author_id=author1.id)

    book3 = Book(title="Code & Coffee", royalty_per_sale=75, author_id=author2.id)
    book4 = Book(title="Startup Diaries", royalty_per_sale=50, author_id=author2.id)
    book5 = Book(title="Poetry of Pain", royalty_per_sale=30, author_id=author2.id)

    book6 = Book(title="Garden of Words", royalty_per_sale=40, author_id=author3.id)

    db.session.add_all([book1, book2, book3, book4, book5, book6])
    db.session.commit()
    
    sales_data = [
        # Silent River
        Sale(book_id=book1.id, quantity=25, sale_date="2025-01-05"),
        Sale(book_id=book1.id, quantity=40, sale_date="2025-01-12"),

        # Midnight in Mumbai
        Sale(book_id=book2.id, quantity=15, sale_date="2025-01-08"),

        # Code & Coffee
        Sale(book_id=book3.id, quantity=60, sale_date="2025-01-03"),
        Sale(book_id=book3.id, quantity=45, sale_date="2025-01-15"),

        # Startup Diaries
        Sale(book_id=book4.id, quantity=30, sale_date="2025-01-10"),

        # Poetry of Pain
        Sale(book_id=book5.id, quantity=20, sale_date="2025-01-18"),

        # Garden of Words
        Sale(book_id=book6.id, quantity=10, sale_date="2025-01-20"),
    ]

    db.session.add_all(sales_data)
    db.session.commit()

    print("Seed data inserted successfully! 🌱")
