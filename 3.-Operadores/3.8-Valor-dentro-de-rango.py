valor = int(input("Escribe el valor: "))
minimo = 0
maximo = 5

rango = valor >= minimo and valor <= maximo

if rango:
    print(f'El valor {valor} estan dentro del rango')
else:
    print(f'El valor {valor} esta fuera del rango')
