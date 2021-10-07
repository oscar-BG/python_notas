"""
    Diccionario
"""
# Los diccionarios cuenta con una lleva que contiene un valor, llaves duplicadas sobreescribe el ultimo valor

# dict (key, value)
diccionario = {
    'IDE': 'Integreted Development Encironment',
    'OOP': 'Object Orientes Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

# Conocer el tamaño
print(len(diccionario))

# Acceder a los elmentos con la llave
print(diccionario['IDE'])

# Otra forma
print(diccionario.get('OOP'))

# Modificando elemento
diccionario['IDE'] = 'Hola'
print(diccionario)

"""
    Leccion 2
"""

# Recorrer los elemento
for termino in diccionario:
    print(termino) #key

# Recorrer el valor
for termino, valor in diccionario.items():
    print(termino, valor)

# Recuperar llaves
for termino in diccionario.keys():
    print(termino)

# Recuperar los valores
for valor in diccionario.values():
    print(valor)

# Existencia de algun elemento
print('IDE' in diccionario)
print('IdE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario