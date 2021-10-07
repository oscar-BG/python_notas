"""
    Diccionario
"""
# Los diccionarios cuenta con una lleva que contiene un valor

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