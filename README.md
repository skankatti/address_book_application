# Address Book API (FastAPI)

## Overview

This project is a simple **Address Book REST API** built using **FastAPI**.
It allows API users to **create, update, delete, retrieve, and search addresses based on geographic distance**.

The application stores addresses with **latitude and longitude coordinates** in a **SQLite database** and provides an API to retrieve addresses within a given distance.

Swagger UI is available for easy API testing.

---

# Features

* Create address
* Update address
* Delete address
* Get all addresses
* Retrieve addresses within a given distance from coordinates
* Input validation using Pydantic
* SQLite database with SQLAlchemy ORM
* Distance calculation using Geopy

---

# Project Structure

```
address-book-api
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   │
│   ├── models
│   │     └── address_model.py
│   │
│   ├── schemas
│   │     └── address_schema.py
│   │
│   ├── services
│   │     └── address_service.py
│   │
│   ├── routes
│   │     └── address_routes.py
│   │
│   └── utils
│         └── distance_utils.py
|
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Prerequisites

Make sure the following are installed:

* Python 3.10+
* pip
* Git

---

# Step 1 — Clone the Repository

```
Create a blank folder to clone the project
```

```
git clone https://github.com/skankatti/address_book_application.git
```

Navigate to the project directory:

---

# Step 2 — Create Virtual Environment

Create virtual environment in project directory:

```
python -m venv venv
```

Activate virtual environment.

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

# Step 3 — Install Dependencies

Install all required packages:

```
pip install -r requirements.txt
```

---

# Step 4 — Configure Environment Variables

Create a `.env` file in the project root.

Example:

```
DATABASE_URL=sqlite:///./address.db
```

---

# Step 5 — Run the Application

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates Swagger documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

You can test all APIs directly from Swagger UI.

---

# Available API Endpoints

### Get All Addresses

```
GET /addresses
```

Returns all saved addresses.

---

### Create Address

```
POST /addresses
```

Example request body:

```
{
  "name": "Home",
  "street": "MG Road",
  "city": "Pune",
  "latitude": 18.5204,
  "longitude": 73.8567
}
```

---

### Update Address

```
PUT /addresses/{address_id}
```

Updates an existing address.

---

### Delete Address

```
DELETE /addresses/{address_id}
```

Deletes an address.

---

### Get Nearby Addresses

```
GET /addresses/nearby
```

Example:

```
/addresses/nearby?lat=18.5204&lon=73.8567&distance=5
```

Returns addresses within **5 km radius**.

---

# Dependencies

Main libraries used:

* FastAPI
* SQLAlchemy
* Pydantic
* Geopy
* python-dotenv
* Uvicorn

---
