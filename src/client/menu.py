# Archivo dedicado a la creación de los distintos menús

def menu_principal() -> int:

    print("\n\n#################################")
    print("  Top 100 libros de la historia")
    print("#################################")    
    print("Seleccione la accion a realizar:")
    print("1. Mostrar todos los libros")
    print("2. Buscar un libro en específico")
    print("3. Agregar un nuevo libro")
    print("4. Eliminar un libro")
    print("5. Salir")

    try: 
        accion = int(input())
        return accion
    except ValueError:
        print("\nPor favor, seleccione una opción valida.\n")


def menu_get_book_by()-> int:
    
    print("Puede buscar un libro por:")
    print("1. Autor")
    print("2. Titulo")
    print("3. Pais")
    print("4. Lenguaje")
    print("5. Año de publicación")
    
  
    accion = input()
    return accion

        
    
    

