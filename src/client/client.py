from menu import (menu_principal,
                  menu_get_book_by)
from auxiliar_client import (check_server_status,
                            get_all_books,
                            get_book_by,
                            post_book,
                            delete_book,
                            HOST,
                            PORT)
import requests
from typing import List, Dict, Any 

   
def main():

    check_server_status()

    while True:         
        
        accion = menu_principal()
                   
        if accion == 1:
            # Devolver todos los libros
            get_all_books()

        elif accion == 2:
            # Buscar libros por autor, titulo, pais, fecha de publicacion o lenguaje
            try:
                seleccion = int(menu_get_book_by())
            except ValueError:
                print("Seleccione una opción valida")
            
            if seleccion == 1:
                get_book_by(author = input("Escriba el nombre del autor: "))
                
            elif seleccion  == 2: 
                get_book_by(title= input("Escriba el título del libro: "))

            elif seleccion == 3: 
                get_book_by(country = input("Escriba el pais de origen: "))

            elif seleccion == 4: 
                get_book_by(language= input("Escriba el lenguaje deseado: "))

            elif seleccion == 5:
                try:
                    get_book_by(year = int(input("Ingrese el año de publicación: ")))
                except ValueError:
                    print("Eliga una fecha válida.")
            
            else:
                print("Selección erronea. Eliga una opción válida.")
                        
        elif accion == 3: 
            # Agregar un nuevo libro al archivo
            post_book()
            continue
        elif accion == 4:
            # Eliminar un libro del archivo
            delete_book()
            continue
        elif accion == 5:
            # Salir
            break
        else: 
            print("Ingrese una opción válida")



main()