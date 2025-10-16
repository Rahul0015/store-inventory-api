from flask import Blueprint, request, jsonify
from database import db
from models import Product
from schemas import ProductSchema
from marshmallow import ValidationError

bp = Blueprint('api', __name__)

# Initialize schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# ------------------ CREATE ------------------
@bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        # ✅ Validate data using Marshmallow
        validated_data = product_schema.load(data)
        new_product = Product(**validated_data)

        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Product created successfully",
            "data": product_schema.dump(new_product)
        }), 201

    except ValidationError as err:
        return jsonify({"status": "error", "errors": err.messages}), 400

    except Exception:
        db.session.rollback()
        raise  # Let the global error handler in app.py handle it



# ------------------ READ (ALL) ------------------
@bp.route('/products', methods=['GET'])
def get_products():
    # ✅ Pagination support
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)

    paginated_products = Product.query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        "status": "success",
        "page": page,
        "limit": limit,
        "total_products": paginated_products.total,
        "total_pages": paginated_products.pages,
        "data": products_schema.dump(paginated_products.items)
    }), 200


# ------------------ READ (BY ID) ------------------
@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"status": "error", "message": "Product not found"}), 404

    return jsonify({
        "status": "success",
        "data": product_schema.dump(product)
    }), 200


# ------------------ UPDATE ------------------
@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"status": "error", "message": "Product not found"}), 404

    try:
        data = request.get_json()
        validated_data = product_schema.load(data, partial=True)  # ✅ Allow partial update

        for key, value in validated_data.items():
            setattr(product, key, value)

        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Product updated successfully",
            "data": product_schema.dump(product)
        }), 200

    except ValidationError as err:
        return jsonify({"status": "error", "errors": err.messages}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 400


# ------------------ DELETE ------------------
@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"status": "error", "message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product deleted successfully"
    }), 200

