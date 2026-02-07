# 📚 BookFlow — Author Royalty Management API

A backend REST API system built with **Flask + SQLite** for managing authors, books, royalties, sales, and withdrawal requests.  
This project simulates a real-world **author royalty and payout system** used in publishing platforms.

> Designed as a clean, production-style backend project with proper architecture, validations, and business rules.

---

## 🚀 Features

- 👩‍💻 Author management  
- 📖 Book royalty tracking  
- 📊 Sales recording  
- 💰 Automatic earnings calculation  
- 🏦 Wallet balance system  
- 💸 Withdrawal requests  
- 📜 Withdrawal history  
- 🔐 Business rule validations  
- 🌍 CORS enabled API  
- 🗄 SQLite database  
- ⚙ Production deployment ready (Gunicorn + Render)

---

## 🧠 Use Cases

- Publishing platforms  
- Author payout systems  
- Royalty tracking services  
- FinTech-style wallet systems  
- Learning REST API architecture  
- Backend portfolio project  
- API automation testing practice  
- Interview-ready backend project  

---

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **ORM**: Flask-SQLAlchemy
- **Server**: Gunicorn
- **CORS**: Flask-CORS
- **Deployment**: Render (Free Tier)
- **Architecture**: Modular MVC-style structure

---

## 📁 Project Structure

BookFlow/
│
├── bookflow/                # Main application package
│   ├── app.py               # Main Flask app + API routes
│   ├── models.py            # Database models
│   ├── config.py            # Database configuration
│   ├── init_db.py           # One-time database initialization
│   ├── seed_data.py              # Seed data insertion
│   └── database.db          # SQLite database file
│
├── requirements.txt
└── README.md
├── LICENSE
└── .gitignore

## ⚙ Setup Commands

### 1️⃣ Clone Repository
```bash
git clone https://github.com/AjayKumar095/BookFlow.git
cd BookFlow


python -m venv .venv
.venv\Scripts\activate  # windows

source .venv/bin/activate # linux/mac

pip install -r requirements.txt
python bookflow/init_db.py

python bookflow/seed.py

python bookflow/app.py
gunicorn bookflow.app:app
```

🌍 API Use Cases & Endpoints
🔹 Get All Authors

Endpoint

GET /authors


Use Case
Retrieve all authors with their total earnings and current wallet balance.

Response Fields

id

name

total_earnings

current_balance

🔹 Get Single Author Details

Endpoint

GET /authors/{id}


Use Case
View complete author profile including books, sales performance, and royalty earnings.

Includes

Author profile

Book list

Royalty per book

Sales totals

Total earnings

Wallet balance

Error

404 if author not found

🔹 Get Author Sales History

Endpoint

GET /authors/{id}/sales


Use Case
Track all sales transactions for an author across all their books, sorted by latest sale.

Fields

book_title

quantity

royalty_earned

sale_date

🔹 Create Withdrawal Request

Endpoint

POST /withdrawals


Request Body

{
  "author_id": 1,
  "amount": 2000
}


Use Case
Allows an author to withdraw money from their royalty balance.

Business Rules

Minimum withdrawal: ₹500

Cannot exceed current balance

Author must exist

Success

Withdrawal status = pending

Balance updated

Returns new balance

HTTP 201

🔹 Get Withdrawal History

Endpoint

GET /authors/{id}/withdrawals


Use Case
View all withdrawal requests made by an author.

Fields

id

amount

status

created_at
