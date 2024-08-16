"""
File: routes.py
Author: Aniket Kale
Email: kaleaniket45@gmail.com
Date Created: 2024-08-16
Last Modified: 2024-08-16

This module defines the API endpoints for the Flask application. It includes endpoints for fetching mock data, processing it, storing the processed data in-memory, and retrieving the processed data.

"""


from flask import Blueprint, jsonify, request
from .data_processor import process_data
from .data_store import store_data, get_stored_data

# Blueprint
main_bp = Blueprint('main', __name__)

# Mock Data
mock_data = [
    {'id': 1, 'name': 'Kangaroo', 'quantity': 5},
    {'id': 2, 'name': 'Camel', 'quantity': 3},
    {'id': 3, 'name': 'Lion', 'quantity': 7}
]

@main_bp.route('/fetch-data', methods=['GET'])
def fetch_data():
    """
    Fetch data from a mock external service, process it, and store it in memory.

    This function simulates the retrieval of data from an external service like shopify.
    The retrieved data is then processed and stored in temporary in-memory storage.

    Returns:
        Response: JSON response with a success message.
    """

    processed_data = process_data(mock_data)
    store_data(processed_data)
    return jsonify({"message": "Data fetched and processed successfully!"}), 200



@main_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """
    Retrieve and return the processed data stored in memory.

    This function returns the processed data that was previously stored in memory
    after being fetched and processed.

    Returns:
        Response: JSON response with the processed data.
    """

    data = get_stored_data()
    return jsonify(data), 200
