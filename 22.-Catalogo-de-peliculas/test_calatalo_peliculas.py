from dominio.pelicula import Pelicula
from servicio.catalogo_pelicula import CatalogoPeliculas as catalogo

opcion = None

while opcion != 4:
    try:
        print('Opciones')
        print('1.- Agregar peliculas')
        print('2.- Listar peliculas')
        print('3.- Eliminar catálogo de peliculas')
        print('4.- Salir')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == 2:
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa')