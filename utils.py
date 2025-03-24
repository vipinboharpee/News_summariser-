import os
import json
import requests
from datetime import datetime

# Function to create a cache directory if not exists
def create_cache_dir():
    cache_dir = "cache"
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

# Clean text function
def clean_text(text):
    return text.strip().replace("\n", " ").replace("\r", "")

# Truncate text to a specific length
def truncate_text(text, max_length=500):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

# Save data to JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Get cached data if available
def get_cached_data(cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as file:
            return json.load(file)
    return None
