from fastapi import FastAPI, HTTPException
from typing import IO, Any
from auxiliar import (get_files,
                      books_json,
                      DATA_PATH,
                      BOOKS_PATH,
                      BookSchema)
import os
import json 
import uvicorn


get_files()

app = FastAPI()

# Confirmación server encendido 
@app.get('/', tags = ["Test"])
def server_running():
    status =  'Server is running!'
    return status


# Devuelve todos los libros 
@app.get('/all_books', tags = ["File handle"])
def get_all_books():
    books = books_json()
    return books


# Devuelve los libros que cumplen con los parámetros 
@app.get('/get_book_by', tags = ["File handle"])
def get_book_by(author : str | None = None, country: str | None = None, language: str | None = None, title: str | None = None, year: int | None = None):

    books_file: IO[Any] | None =  books_json()
    books_by_parameter: list[dict[str, Any]] = []

    for book in books_file:
        
        if book.get('author') == author and author != None: 
            books_by_parameter.append(book)
            continue
        
        if book.get('country') == country and country != None: 
            books_by_parameter.append(book)
            continue

        if book.get('language') == language and language != None: 
            books_by_parameter.append(book)
            continue

        if book.get('year') == year and year != None: 
            books_by_parameter.append(book)
            continue

        if book.get('title') == title and title != None: 
            books_by_parameter.append(book)               
            continue

    if books_by_parameter == []:
        return {"error": "No se ha encontrado ningún libro que cumpla con las características!"}
    else: 
        return books_by_parameter


# Agrega un nuevo libro al archivo 
@app.post("/post_book", tags= ["File handle"])
def post_book(book : BookSchema): 
    
    try:
        with open(BOOKS_PATH, "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="El archivo no existe o no se ha encontrado")

    # Verificar si el libro ya existe para evitar duplicados
    for b in books:
        if b["title"] == book.title and b["author"] == book.author:
            raise HTTPException(status_code=400, detail="El libro ya se encuentra en la base de datos")
    

    books.append(book.model_dump())

    with open(BOOKS_PATH, "w") as file:
        json.dump(books, file, indent=4)

    return book    

if __name__ == "__main__":
    uvicorn.run('server:app', reload=True)


# Elimina el libro que cumple con los parámetros
@app.post("/delete_book", tags = ["File handle"])
def delete_book(title: str, author: str):
    
    try:
        with open(BOOKS_PATH, "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="El archivo no existe o no se ha encontrado")
    
    for b in books:
        
        if b["title"] == title and b["author"] == author: 
            books.remove(b)
            
            with open(BOOKS_PATH, "w") as file:
                json.dump(books, file, indent=4)
            
            return {"Libro eliminado con éxito"}                

    raise HTTPException(status_code=400, detail="El libro no se ha encontrado")

