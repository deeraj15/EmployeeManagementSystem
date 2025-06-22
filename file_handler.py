# file_handler.py

import json

FILE_NAME = 'employees.json'

def load_employees():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_employees(employee_list):
    with open(FILE_NAME, 'w') as file:
        json.dump(employee_list, file, indent=4)
