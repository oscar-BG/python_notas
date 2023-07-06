from Manejo_archivo import *

# with: contexto de nuestro archivo cierra de manera automatica nuestro archivo
# archivo: renombramos la respuesta
# r: leesmo el contenido de nuestro archivo

#with open('prueba.txt', 'r', encoding='utf-8') as archivo:
#    print(archivo.read())


with ManejoArchivo('prueba.txt') as archivo:
    print(archivo.read())