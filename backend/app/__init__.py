from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configure the Flask application
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost/equipmentcentral')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize CORS
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import models to ensure they are registered with SQLAlchemy
    from .models import User, Operator, EquipmentCategory, Equipment
    
    # Register blueprints
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

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
