"""
Crer una funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos
"""

def multiplicar(*args):
    r_multiplicacion = 1
    for numero in args:
        r_multiplicacion *= numero

    return r_multiplicacion

# Lllamar a la funcion
print(multiplicar(2,3))