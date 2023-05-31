# Funciones recursivas

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero -1)

resultado = factorial(15)
print(f'Resultado ${resultado}')