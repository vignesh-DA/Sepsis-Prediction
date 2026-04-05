"""
Common Utility Functions
"""
import os
import joblib
import yaml

def save_object(file_path, obj):
    """Save object to file"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    joblib.dump(obj, file_path)

def load_object(file_path):
    """Load object from file"""
    return joblib.load(file_path)

def read_yaml(file_path):
    """Read YAML file"""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
