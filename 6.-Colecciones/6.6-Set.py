"""
    Set
"""
# No mantiene un order, no soporta elementos duplicados pero si se puede eliminar

planetas = {'Marte','Jupiter', 'Venus'}

print(planetas)
# Conocer el tamaño
print(len(planetas))

# Revisar si un elemento esta presente
print('Marte' in planetas)
print('Martes' in planetas)

# Agregar nuevos elementos
planetas.add('Tierra')
print(planetas)

# No se puede duplicar elmentos
planetas.add('Tierra')
print(planetas)

# Elimar elementos, si no existe manda error
planetas.remove('Tierra')
print(planetas)

#Elimnar sin error
planetas.discard('Jupiter')
print(planetas)
planetas.discard('Jupi')

#Limpiar el set
planetas.clear()
print(planetas)

# Elimanar por completo
del planetas