"""
Tarea: 
1.- Crear una funcion para sumar los valores recibidos de tipo numerico, 
2.- utilizando argumentos varibales *args como parámetro de la funcion 
3.- regresar como resultado la suma de todos los valores pasados como argumentos
"""
def sumar(*numeros):
    suma = 0
    for num in numeros:
        suma += num
    
    return suma

# llamar a la funcion
print(sumar(3,5,9,3))