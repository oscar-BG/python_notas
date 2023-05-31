"""
Imprimir números de 5 a 1 de manera descendete usado funciones recursivas,
"""

def numerosDescendete(numero):
    if numero >= 1:
        print(numero)
        numerosDescendete(numero -1)

numerosDescendete(4)