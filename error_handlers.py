# error_handlers.py
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(400)
    def bad_request_error(e):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"error": "Something went wrong on the server"}), 500
