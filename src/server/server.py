from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from typing import IO, Any, List
from auxiliar import (get_files,
                      books_json,
                      DATA_PATH,
                      BOOKS_PATH,
                      BookSchema)
import os
import json 
import uvicorn
import shutil


HOST = "localhost"
PORT = 8000


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
def get_book_by(author : str | None = None, 
                country: str | None = None, 
                language: str | None = None, 
                title: str | None = None, 
                year: int | None = None):

    books_file: IO[Any] | None =  books_json()
    books_by_parameter= []
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

    return books_by_parameter

# Agregar un nuevo libro al archivo
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

    return f"El libro {book.title} se ha guardado con éxito"


# Elimina el libro que cumple con los parámetros
@app.delete("/delete_book", tags = ["File handle"])
def delete_book(author: str, title: str):
    
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
            
            return f"El libro '{title}' se ha eliminado con éxito"                

    raise HTTPException(status_code=400, detail="El libro no se ha encontrado")



# Devuelve la portada del libro  
@app.get("/get_image", tags=['Image handle'])
def get_image(imageLink :str): 
    
    
    image_url = os.path.join(DATA_PATH, 'images', imageLink)

    if not os.path.exists(image_url):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    
    try:
        file = open(image_url, mode="rb")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al abrir el archivo")
    
    return StreamingResponse(file, media_type="image/jpeg")


# Actualiza la portada de un libro
@app.post("/upload_image" , tags = ['Image handle'])
async def upload_image(image: UploadFile):
    
    image_path = DATA_PATH + f"/images/{image.filename}"
    
    try:
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
            return f"Imagen '{image.filename}' cargada con éxito"
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al guardar la portada")

    

# Borra una imagen de la carpeta images
@app.delete("/delete_image",tags = ["Image handle"])
def delete_image(imageLink : str):
    
    image_path = os.path.join(DATA_PATH, imageLink)
    
    try:
        if os.path.exists(image_path):
            os.remove(image_path)
            return f"La portada ubicada  en '{image_path}' ha sido borrado con éxito."
        else:
            return f"No se encontró '{image_path}'."
    except Exception as e:
        print(f"Error al borrar el archivo: {e}")



if __name__ == "__main__":
    uvicorn.run('server:app', host= HOST, port=PORT,  reload=True)
