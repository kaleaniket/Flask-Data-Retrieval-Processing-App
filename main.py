"""
File: main.py
Author: Aniket Kale
Email: kaleaniket45@gmail.com
Date Created: 2024-08-16
Last Modified: 2024-08-16

This is the entry point for running the Flask application. It initializes the Flask app and runs it on the local server.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
