# score.py

import json

def load_scores(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

