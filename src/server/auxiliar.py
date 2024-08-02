from typing import IO, Any
import requests
import json

import os 
from pydantic import BaseModel


DATA_PATH = os.path.join(os.getcwd(),'src', 'data')
BOOKS_PATH = os.path.join(DATA_PATH, 'books.json')


# Representación de cada objeto libro perteneciente al archivo books.json 
class BookSchema(BaseModel):
    author: str
    country: str
    imageLink: str
    language: str
    link: str
    pages: int
    title: str
    year: int


def get_files():

# Descarga el archivo .json
    
    if not 'books.json' in os.listdir(DATA_PATH):
       
       with open(BOOKS_PATH, 'w') as json_file:
        json.dump(requests.get('https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json').json(), json_file, indent = 4)



def books_json() -> IO[Any] | None: 
   
    with open(BOOKS_PATH, 'r+') as file:
        books = json.load(file)
        return books
