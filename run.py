#!/usr/bin/env python3
"""
FaithConnect - Christian Community App
Run script for development server
"""

from app import app, db
import os

def create_tables():
    """Create database tables"""
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

def run_app():
    """Run the Flask application"""
    # Create tables if they don't exist
    create_tables()
    
    # Get environment settings
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.getenv('FLASK_PORT', 5000))
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    
    print(f"Starting FaithConnect on {host}:{port}")
    print(f"Debug mode: {debug_mode}")
    print("Press Ctrl+C to stop the server")
    
    app.run(host=host, port=port, debug=debug_mode)

if __name__ == '__main__':
    run_app()