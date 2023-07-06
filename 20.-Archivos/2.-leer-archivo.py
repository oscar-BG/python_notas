#r para leer el archivo
archivo = open('prueba.txt', 'r', encoding='utf-8')
#print(archivo.read())


##### LEER ARGUNOS CARACTERES

# Leer los primeros 5 caracteres
#print(archivo.read(5))
# Leer los siguientes 4 caracteres
#print(archivo.read(4))

##### LEER LINEAS COMPLETAS

#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())

### ITERAR EL ARCHIVO

#for linea in archivo:
#    print(linea)

### LEER LINEAS
#print(archivo.readlines())  #Devuel una lista

# Aceder a una linea de la lista
#print(archivo.readlines()[1])

## Copiar archivo
archivo2 = open('copia.txt', 'a', encoding='utf-8')

archivo2.write(archivo.read())

archivo2.close()
archivo.close()