import requests
import json
import os 

DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), 'data')
BOOKS_PATH = os.path.join(DATA_PATH, 'books.json')

def get_json():

# Descarga el archivo .json
    
    if not 'books.json' in os.listdir(DATA_PATH):
       
       with open(BOOKS_PATH, 'w') as json_file:
        json.dump(requests.get('https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json').json(), json_file, indent = 4)



