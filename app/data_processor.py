"""
File: data_processor.py
Author: Aniket Kale
Email: kaleaniket45@gmail.com
Date Created: 2024-08-16
Last Modified: 2024-08-16

This module contains functions for processing data. The current implementation performs a simple transformation on the data.
"""


def process_data(data):
    """
    Process the data by converting all 'name' fields to uppercase.

    Args:
        data (list of dict): The data to be processed.

    Returns:
        list of dict: The processed data with names in uppercase.
    """
    for item in data:
        item['name'] = item['name'].upper()
    return data
