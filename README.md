# Library Management API

This is a Library Management System API built with Flask, SQLAlchemy, PostgreSQL, Swagger UI for API documentation, and pytest for testing.

## Features

- **Authors API**: Manage authors (CRUD operations)
- **Books API**: Manage books (CRUD operations)
- **Swagger UI**: Auto-generated API documentation
- **Pytest**: Automated testing for API routes
- **PostgreSQL**: Database setup for managing library data

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [API Documentation with Swagger](#api-documentation-with-swagger)
5. [Database Migrations](#database-migrations)
6. [Running Tests with Pytest](#running-tests-with-pytest)

## Requirements

- Python 3.x
- PostgreSQL
- Virtual Environment (recommended)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api

python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

pip install -r requirements.txt

#setup postgresql
CREATE DATABASE library_db;
#go to .env file
DATABASE_URL=postgresql://yourusername:yourpassword@localhost:5432/library_db
SECRET_KEY=your-secret-key


#running the project
python run.py

#API Documentation
http://127.0.0.1:5000/apidocs/


#Database Migration
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


#running pytest
pytest
```
## Running Locust Load Test
```bash
locust -f locustfile.py --headless -u 100 -r 10 --run-time 1m --host http://127.0.0.1:5000 --csv=locust_output
```

## Project Structure

library-management-api/
│
├── app/
│   ├── __init__.py        # Initializes the Flask app
│   ├── models.py          # SQLAlchemy models for Author and Book
│   ├── authors/
│   │   ├── __init__.py    # Blueprint for authors
│   │   ├── routes.py      # Routes for authors
│   │   └── services.py    # Business logic for authors
│   ├── books/
│   │   ├── __init__.py    # Blueprint for books
│   │   ├── routes.py      # Routes for books
│   │   └── services.py    # Business logic for books
│   └── utils.py           # Utility functions
│
├── migrations/            # Database migrations
├── tests/                 # Automated tests
├── seed.py                # Seeder script for populating the database with dummy data
├── locustfile.py          # Load testing with Locust
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── run.py                 # Main entry point to run the app
└── README.md              # Project documentation





---

Once you've created this file, it will guide anyone who wants to set up, run, or contribute to your project. &#8203;:contentReference[oaicite:0]{index=0}&#8203;
