# Declarar un lista
nombre = ['Oscar','Marta','Cecilia',1,100]

# Imprimir la lista de nombres
print(nombre)

# Acceder a un elemento de la lista
print(nombre[0])
print(nombre[1])
print(nombre[2])

# Imprimir un rango
print(nombre[0:2]) #Sin incluir el indice 2
# Ir del inicio de la lista al índice (Sin incluirlo)
print(nombre[:3])
# Desde el indice indicado hasta el final
print(nombre[1:])
# Cambiar un valor
nombre[3] = 'Nuevo'
print(nombre)
# Iterar una lista
for nombres in nombre:
    print(nombre)
else: 
    print('No existe más nombres en la lista')

#Preguntar el largo de una lista
print(f"tamaño de la lista nombre:  {len(nombre)}")

#Agregar un elemento
nombre.append('Lorenzo')
print(nombre)
#Insertar un elemento en un ídice es especifico
nombre.insert(1,'Octavio')
print(nombre)
#Remover un elemento
nombre.remove('Octavio')
print(nombre)
#Remover el último valor agregado
nombre.pop()
print(nombre)
#Eliminar un elemnto en un índice indicado
del nombre[0]
print(nombre)
#Limpiar todos los elementos de la lista
nombre.clear()
print(nombre)
# Borrar la lista por completo
del nombre
print(nombre)