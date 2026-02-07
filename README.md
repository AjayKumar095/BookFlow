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
├── bookflow/
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   ├── init_db.py
│   ├── seed.py
│   └── database.db
│
├── requirements.txt
└── README.md



## ⚙ Setup Commands

### 1️⃣ Clone Repository
```bash
git clone https://github.com/AjayKumar095/BookFlow.git
cd BookFlow
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
```
### 3️⃣Activate Environmnent
``` bash
.venv\Scripts\activate  # windows
source .venv/bin/activate # linux/mac
```
### 4️⃣Install Requirements
``` bash
pip install -r requirements.txt
```
### 5️⃣Project Initiate Commands
```bash
python bookflow/init_db.py

python bookflow/seed.py

python bookflow/app.py
```
### 🌍 API Use Cases & Endpoints
```bash
BASE URL http://127.0.0.1:5000
```
### 🔗 API's Endpoints
* GET /authors
```bash
# Use Case
# Retrieve all authors with their total earnings and current wallet balance.

# Response Fields
[
    {
        "current_balance": 2825,
        "id": 1,
        "name": "Priya Sharma",
        "total_earnings": 3825
    },
    {
        "current_balance": 9975,
        "id": 2,
        "name": "Rahul Verma",
        "total_earnings": 9975
    },
    {
        "current_balance": 400,
        "id": 3,
        "name": "Anita Desai",
        "total_earnings": 400
    }
]
```
* GET /authors/{id}
``` bash
# Use Case
# View complete author profile including books, sales performance, and royalty earnings.

# Response Fields

# Success
# tested for /authors/3
{
    "books": [
        {
            "id": 6,
            "royalty_per_sale": 40,
            "title": "Garden of Words",
            "total_royalty": 400,
            "total_sold": 10
        }
    ],
    "current_balance": 400,
    "email": "anita@email.com",
    "id": 3,
    "name": "Anita Desai",
    "total_books": 1,
    "total_earnings": 400
}

# Error
# in case author not found

{
    "error": "404 Not Found"
}
```
* GET /authors/{id}/sales
```bash
# Use Case
# Track all sales transactions for an author across all their books, sorted by the latest sale.

# Response Fields

# Success
# tested for /authors/1/sales
[
    {
        "book_title": "The Silent River",
        "quantity": 40,
        "royalty_earned": 1800,
        "sale_date": "2025-01-12"
    },
    {
        "book_title": "Midnight in Mumbai",
        "quantity": 15,
        "royalty_earned": 900,
        "sale_date": "2025-01-08"
    },
    {
        "book_title": "The Silent River",
        "quantity": 25,
        "royalty_earned": 1125,
        "sale_date": "2025-01-05"
    }
]

# Error
# in case author not found

{
    "error": "404 Not Found"
}
```
* POST /withdrawals
```bash
# Request Body

{
  "author_id": 1,
  "amount": 1000
}
```
```bash
# Use Case
# Allows an author to withdraw money from their royalty balance.

# Business Rules
# If withdrawal amount is less than: ₹500
{
    "error": "Minimum withdrawal amount is ₹500"
}

# If withdrawal amount is greater than current_balance 
{
    "error": "Insufficient balance"
}

# if author does not exist
{
    "error": "Author not found."
}

# Success
{
    "amount": 1000,
    "author_id": 1,
    "id": 3,
    "new_balance": 1825,
    "status": "pending"
}

```
* GET /authors/{id}/withdrawals
```bash
# Use Case
# View all withdrawal requests made by an author.


# Response Fields
[
    {
        "amount": 1000,
        "created_at": "2026-02-07 13:04:05",
        "id": 3,
        "status": "pending"
    },
    {
        "amount": 500,
        "created_at": "2026-02-07 12:05:19",
        "id": 2,
        "status": "pending"
    },
    {
        "amount": 500,
        "created_at": "2026-02-07 11:59:51",
        "id": 1,
        "status": "pending"
    }
]
```
