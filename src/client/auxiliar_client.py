# Archivo para las funciones necesarias para el cliente

import requests
import json
from typing import List, Dict, Any 

HOST: str = 'http://192.168.100.18'
PORT: str = '8000' 

url =  HOST + ':' + PORT

def get_all_books() -> List[Dict[str, Any]]: 
    # Muestra en pantalla y devuelve todos los libros
    
    response = requests.get(f"{url}/all_books")
    if response.status_code == 200:
        books: dict = json.loads(response.text)
        if books != []:
            for book in books:
                print("----------------------")
                print(f"'{book.get('title')}' de {book.get('author')}")
                print(f"Publicado en {book.get('year')}, cuenta con {book.get('pages')} páginas")

    return books

def get_book_by(author : str | None = None, 
                country: str | None = None, 
                language: str | None = None,
                title: str | None = None, 
                year: int | None = None) -> List[Dict[str, Any]]:
    # Muestra en pantalla y devuelve los libros que cumple con el parametro establecido

    response  = requests.get(f"{url}/get_book_by", params = {'author' : author, 
                                                             'country' : country, 
                                                             'language': language, 
                                                             'title':title, 
                                                             'year':year})
    
    
    if response.status_code == 200:
        
        books: List[Dict[str, Any]] = json.loads(response.text)
        if books != []:
            for book in books:
                print("----------------------")
                print(f"'{book.get('title')}' de {book.get('author')}")
                print(f"Publicado en {book.get('year')}, cuenta con {book.get('pages')} páginas")
        else: 
            print("No se encontró ningun libro con esas caracterísitcas")
    return books            


def post_book():
    # Agrega un nuevo libro a la base de datos

    title = input("Nombre del libro: ")
    author = input("Nombre del autor: ")
    language = input("Idioma del libro: ")
    country = input("Pais: ")
    while True:
        try:
            year = int(input("Anio de publicacion: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    while True:    
        try:
            pages = int(input("Cantidad de páginas: "))
            break
        except ValueError:
            print("Ingrese un número válido.")   
    
    link = input("Link de refencia: ")
    image = input('Nombre del archivo de su portada (images\nombre-archivo.jpg): ') 

    book  : dict = {
        "author": author,
        "country": country,
        "imageLink": image,
        "language": language,
        "link": link,
        "pages": pages,
        "title": title,
        "year": year
    }

    response = requests.post(url + "/post_book", json = book)
    if response.status_code == 200:
        print(response.json())
        print("Cargar portada? [S] Si   [N] No ")
        cargar = input()
        if cargar == "S" or cargar == "s": 
            
            image_path = input("Ingrese la ubicacion de la imagen (Recordar que el nombre del archivo debe coincidir con lo administrado anteriormente)")
            
            with open(image_path, "rb") as image_file:
                
                file = {"image": image_file}
                response = requests.post(url + "/upload_image", files=file)
                if response.status_code == 200:
                    print("Portada cargada con éxito")
                else: 
                    print("Error al cargar la portada")    
    else:
        print(f"Error: {response.status_code}")
        
    
def delete_book():
    # Elimina un libro de la base de datos junto a su portada
    
    title = input("Ingrese el título a eliminar: ")
    author = input("Ingrese el nombre del autor: ")
    book = get_book_by(title = title)    
    response = requests.post(url + "/delete_book", params={'author':author, 'title' : title})
    
    if response.status_code == 200:
        print(response.json())
        
        delete_image_response = requests.post(url + "/delete_image", params ={"imageLink": book[0].get('imageLink')})
        print(delete_image_response.json())

    