# Definir una tupla
# Las tuplas no se les puede agregar o mever su informacion

frutas = ('Naranja','Platano','Guayaba')

#Conocer el tamaño
print(len(frutas))

# Acceder a un dato
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:1]) #Sin incluir el ultimo indice

# Recorrer elementos

for fruta in frutas:
    print(fruta, end=' ') #end=(' ') muestra todos los elemento en una sola liena

# Cambiar el valor tupla
# frutas[0] = "Pera" no se puede cambiar el valor de una tupla
# print(frutas)

#Modificar los elemento

# 1.-  Cambiar nuestra tupla a una lista
frutasLista = list(frutas)
# 2.- Modificar el valor
frutasLista[0] ='Pera'
# 3.- Cambiar nuestra lista a tupla
frutas = tuple(frutasLista)
print('\n', frutas)

# Eliminar una tupla
del frutas



