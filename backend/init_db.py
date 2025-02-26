from flask_migrate import init, migrate, upgrade
from app import create_app, db
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def init_database():
    # Create database if it doesn't exist
    try:
        # Connect to PostgreSQL server
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='equipmentcentral'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE equipmentcentral")
            print("Database 'equipmentcentral' created successfully!")
        
        cursor.close()
        conn.close()
        
        # Connect to the equipmentcentral database
        conn = psycopg2.connect(
            dbname='equipmentcentral',
            user='postgres',
            password='postgres',
            host='localhost'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Enable uuid-ossp extension (we don't need PostGIS anymore)
        cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
        print("PostgreSQL extensions enabled successfully!")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error setting up database: {str(e)}")
        return
    
    # Initialize Flask app and create tables
    app = create_app()
    
    with app.app_context():
        # Initialize migrations if they don't exist
        if not os.path.exists('migrations'):
            init()
            print("Migrations directory created!")
        
        # Generate initial migration
        migrate()
        print("Initial migration generated!")
        
        # Apply migration
        upgrade()
        print("Migration applied successfully!")
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_database() 