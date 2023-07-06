try:
    # Abre el archivo o lo crea si no existe
    # encoding='utf-8' Especifica el juego de caracteres
    archivo = open('prueba.txt', 'w', encoding='utf-8')

    #Escribir información en el archivo
    archivo.write('Hola mundo \n')  
    archivo.write('Bienvenido a python \n')
    archivo.write('Información de la clase')
except Exception as e:
    print(f'Error {e}')
finally:
    archivo.close()