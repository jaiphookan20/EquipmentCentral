from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    # Configure the Flask application
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

    # Initialize CORS
    CORS(app)

    # Log requests
    @app.before_request
    def log_request_info():
        logger.info(f'Request: {request.method} {request.url}')

    # Simple test route
    @app.route('/api/test')
    def test_route():
        logger.info('Test endpoint accessed')
        return {'message': 'Flask server is running!'}

    logger.info('Flask application initialized')
    return app
