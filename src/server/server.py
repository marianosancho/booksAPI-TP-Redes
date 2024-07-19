from fastapi import FastAPI
from auxiliar import (get_json,
                      DATA_PATH,
                      BOOKS_PATH)
import os
import json 



get_json()
app = FastAPI()

@app.get('/all_books')
def get_all_books():
    with open(BOOKS_PATH, 'r+') as file:
        books = json.load(file)
        return books 


    

    