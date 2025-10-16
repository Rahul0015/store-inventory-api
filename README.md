# Product Management API

A simple and efficient **RESTful API** built using **Flask**, **SQLAlchemy**, and **Marshmallow**, with a **PostgreSQL** backend.  
It provides CRUD operations for managing products, with input validation, error handling, and JSON-based responses.  
You can easily test all endpoints using **Postman**.

---

##  Features

- Create, Read, Update, and Delete (CRUD) products  
- Input validation using **Marshmallow**  
- Centralized error handling (Validation, Integrity, and Server errors)  
- Lightweight and easy to deploy 
- Modular project structure with Blueprints  
- Fully testable in Postman 
---

##  Project Structure
store_inventory_api/
├── bne the Repositoryackend/
│ ├── init.py
│ ├── app.py # Main Flask app
│ ├── database.py # PostgreSQL connection and initialization
│ ├── models.py # SQLAlchemy Product model
│ ├── schemas.py # Marshmallow validation schemas
│ ├── errors.py # Centralized error handlers
│ ├── routes/
│ │ ├── init.py
│ │ ├── routes.py # Product CRUD API routes
├── requirements.txt
├── README.md


---

##  Setup Instructions

### 1️ Clone Repository

```bash
git clone https://github.com/yourusername/store-inventory-api.git
cd store-inventory-api

### Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

### Install Dependencies

pip install -r requirements.txt

## Configure PostgreSQL Database

psql -U postgres
CREATE DATABASE store_db;

##Update your database configuration in database.py:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_password@localhost/store_db'

##  Run the Flask App
python app.py

✅ The app will start at:
http://127.0.0.1:5000/

---

🧠 API Endpoints
Method	Endpoint	Description
POST	/products	Create a new product
GET	/products	Get all products
GET	/products/<id>	Get a product by ID
PUT	/products/<id>	Update a product
DELETE	/products/<id>	Delete a product
📋 Example JSON Payload
{
  "name": "Laptop",
  "category": "Electronics",
  "quantity": 10,
  "price": 999.99,
  "sku": "LTP123"
}

🧪 Testing with Postman

You can test the API using Postman:

▶️ Create a Product

Method: POST

URL: http://127.0.0.1:5000/products

Body: (raw JSON)

{
  "name": "Mobile",
  "category": "Electronics",
  "quantity": 15,
  "price": 500.0,
  "sku": "KEY103"
}

▶️ Get All Products

Method: GET

URL: http://127.0.0.1:5000/products

▶️ Get Product by ID

Method: GET

URL: http://127.0.0.1:5000/products/1

▶️ Update Product

Method: PUT

URL: http://127.0.0.1:5000/products/1

Body:

{
  "quantity": 20,
  "price": 450.0
}

▶️ Delete Product

Method: DELETE

URL: http://127.0.0.1:5000/products/1

---

⚠️ Error Handling

Error Type	Status Code	Example Response
Validation Error	400	{ "status": "error", "errors": { "price": ["Must be greater than or equal to 0."] }}
Unique Constraint	409	{ "status": "error", "message": "Duplicate SKU detected" }
Not Found	404	{ "status": "error", "message": "Product not found" }
Server Error	500	{ "status": "error", "message": "Internal Server Error" }
🧰 Technologies Used

Flask – Python web framework

Flask-SQLAlchemy – ORM for PostgreSQL

Marshmallow – Validation and serialization

PostgreSQL – Relational database

Postman – API testing tool

🧩 Future Enhancements

🔐 Add JWT-based authentication

📖 Implement pagination and filtering

🌐 Add CORS support for frontend integration

☁️ Deploy to Render / Railway / AWS

🧾 License

This project is open-source under the MIT License.

👨‍💻 Author

Rahul Jaman
💡 Passionate about AI, Data, and Backend Development
📧 rahulj.ds24@duk.ac.in


---



