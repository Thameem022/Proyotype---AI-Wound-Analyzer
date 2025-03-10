from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_error(error):
    """Global error handler for the Flask application."""
    
    if isinstance(error, HTTPException):
        response = {
            "error": error.name,
            "message": error.description,
            "status_code": error.code
        }
        return jsonify(response), error.code

    response = {
        "error": "Internal Server Error",
        "message": str(error),
        "status_code": 500
    }
    return jsonify(response), 500
