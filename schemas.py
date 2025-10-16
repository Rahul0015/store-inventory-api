from marshmallow import Schema, fields, validate, ValidationError

# Custom error messages for better clarity
CUSTOM_MESSAGES = {
    "required": "This field is required.",
    "null": "Field cannot be null.",
    "invalid": "Invalid value provided."
}

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    
    # Name validation
    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100, error="Name must be between 2 and 100 characters."),
        error_messages=CUSTOM_MESSAGES
    )
    
    # Category validation with optional constraints (example)
    category = fields.Str(
        required=True,
        validate=validate.OneOf(
            ["Electronics", "Clothing", "Grocery", "Furniture", "Stationery"],
            error="Category must be one of: Electronics, Clothing, Grocery, Furniture, Stationery."
        ),
        error_messages=CUSTOM_MESSAGES
    )
    
    # Quantity (must be non-negative)
    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=0, error="Quantity cannot be negative."),
        error_messages=CUSTOM_MESSAGES
    )
    
    # Price (must be > 0)
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0.01, error="Price must be greater than 0."),
        error_messages=CUSTOM_MESSAGES
    )
    
    # SKU (unique product code — must be at least 4 characters)
    sku = fields.Str(
        required=True,
        validate=validate.Length(min=4, max=20, error="SKU must be between 4 and 20 characters."),
        error_messages=CUSTOM_MESSAGES
    )
