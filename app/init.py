"""
File: init.py
Author: Aniket Kale
Email: kaleaniket45@gmail.com
Date Created: 2024-08-16
Last Modified: 2024-08-16

This module initializes the Flask application and registers the routes blueprint.
"""

from flask import Flask

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        app (Flask): The configured Flask application instance.
    """    
    app = Flask(__name__)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
