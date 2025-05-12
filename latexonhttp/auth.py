import os
import logging
from functools import wraps
from flask import request, jsonify

logger = logging.getLogger(__name__)

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        expected_api_key = os.environ.get('LATEX_ON_HTTP_API_KEY')
        
        if not expected_api_key:
            logger.warning("No API key configured in environment")
            return jsonify({"error": "API key not configured"}), 500
            
        if not api_key:
            logger.warning("No API key provided in request")
            return jsonify({"error": "API key required"}), 401
            
        if api_key != expected_api_key:
            logger.warning("Invalid API key provided")
            return jsonify({"error": "Invalid API key"}), 401
            
        return f(*args, **kwargs)
    return decorated 