from flask import Flask, jsonify
from routes import bp
from database import init_db
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed

app = Flask(__name__)

# Initialize database and register routes
init_db(app)
app.register_blueprint(bp)

@app.route('/')
def home():
    return {"message": "Welcome to the Store Inventory API!"}

# ---------------- ERROR HANDLING MIDDLEWARE ----------------

# 1️⃣ Integrity Errors (e.g., duplicate SKU, null values in NOT NULL columns)
@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    msg = str(error).lower()
    if 'unique constraint' in msg or 'duplicate key value' in msg:
        message = "SKU already exists. Please use a unique SKU value."
    elif 'not-null constraint' in msg:
        message = "One or more required fields are missing."
    else:
        message = "Database integrity error. Please check your input."
    return jsonify({
        "status": "error",
        "message": message
    }), 400

# 2️⃣ Data Errors (invalid data types, wrong numeric formats, etc.)
@app.errorhandler(DataError)
def handle_data_error(error):
    return jsonify({
        "status": "error",
        "message": "Invalid data type or value. Please check your input fields."
    }), 400

# 3️⃣ Operational Errors (database connection issues, etc.)
@app.errorhandler(OperationalError)
def handle_operational_error(error):
    return jsonify({
        "status": "error",
        "message": "Database operation failed. Please try again later."
    }), 500

# 4️⃣ Bad Request (missing or malformed JSON)
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({
        "status": "error",
        "message": "Bad request. Please check your JSON payload or parameters."
    }), 400

# 5️⃣ Not Found (invalid routes or resources)
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({
        "status": "error",
        "message": "The requested resource was not found."
    }), 404

# 6️⃣ Method Not Allowed (wrong HTTP method)
@app.errorhandler(MethodNotAllowed)
def handle_method_not_allowed(error):
    return jsonify({
        "status": "error",
        "message": "HTTP method not allowed on this endpoint."
    }), 405

# 7️⃣ General Catch-All Exception Handler
@app.errorhandler(Exception)
def handle_general_error(error):
    # Optional: print or log actual error for debugging
    print("Error:", error)
    return jsonify({
        "status": "error",
        "message": "An unexpected error occurred. Please try again later."
    }), 500

# -------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)


