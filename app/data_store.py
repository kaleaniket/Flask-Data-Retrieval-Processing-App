"""
File: data_store.py
Author: Aniket Kale
Email: kaleaniket45@gmail.com
Date Created: 2024-08-16
Last Modified: 2024-08-16

This module defines the API endpoints for the Flask application. It includes endpoints for fetching mock data, processing it, storing the processed data in-memory, and retrieving the processed data.

"""


data_storage = {}

def store_data(data):
    """
    Store the processed data in memory.

    Args:
        data (list of dict): The processed data to be stored.
    """    
    global data_storage
    data_storage = data

def get_stored_data():
    """
    Retrieve the processed data stored in memory.

    Returns:
        list of dict: The stored processed data.
    """    
    return data_storage
