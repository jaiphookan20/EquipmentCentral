from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Initialize SQLAlchemy
db = SQLAlchemy()

# Create a base class for all models
Base = declarative_base() 