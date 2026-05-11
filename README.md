# BMES Project – Full Stack Django E-Commerce System

## 📌 Project Overview

**BMES Project** is a full-stack Django-based e-commerce system built using multiple modular apps.  
It is designed to simulate a real-world production-level web application with separate responsibilities for catalog management, cart handling, checkout, orders, users, and location services.

The system follows a **modular Django architecture**, making it scalable, maintainable, and suitable for enterprise-level applications.

---

## 🏗️ Project Structure

BMESPROJECT/

├── bmestproject/        # Django project configuration (settings, urls, wsgi)

├── app/                 # Core shared app (base utilities / shared logic)

├── cartapp/             # Shopping cart functionality

├── catalogueapp/        # Product catalog and product management

├── checkoutapp/        # Checkout and payment workflow

├── locationapp/        # Location / address handling

├── orderapp/           # Order processing and management

├── userapp/            # User authentication and profile management

├── static/             # Static files (CSS, JS, images)4
├── db.sqlite3          # SQLite database (development)

├── manage.py           # Django project manager

├── requirements.txt    # Project dependencies

├── .gitignore          # Ignored files for version control

├── README.md           # Project documentation


---

## 🎯 Project Goals

This project aims to:

- Build a **real-world e-commerce system** using Django
- Practice **multi-app architecture design**
- Implement full **CRUD operations across multiple modules**
- Manage **user authentication and sessions**
- Handle **shopping cart and order lifecycle**
- Integrate **checkout workflow**
- Manage **product catalog system**
- Work with **modular and scalable backend design**

---

## 🧠 Key Features

### 👤 User Management (`userapp`)
- User registration and login
- Profile management
- Authentication system

### 🛍️ Product Catalog (`catalogueapp`)
- Product listing
- Product details
- Category-based browsing

### 🛒 Cart System (`cartapp`)
- Add/remove items
- Quantity management
- Cart persistence per user

### 💳 Checkout System (`checkoutapp`)
- Order summary
- Checkout workflow
- Order validation

### 📦 Order Management (`orderapp`)
- Order creation
- Order tracking
- Order history

### 📍 Location Services (`locationapp`)
- Address handling
- Delivery location management

---

## 🛠️ Technologies Used

- Python 3
- Django Framework
- SQLite (development database)
- HTML5 / CSS3
- JavaScript
- Bootstrap (UI styling)
- Git & GitHub

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd BMESPROJECT