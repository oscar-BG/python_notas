#### OPERADORES LOGICOS ####

# and, Devuelve True si ambos operandos son True
# or, Devuelve True si alguno de los operandos es True
# not, Devuelve True si alguno de los operandos es False y viseversa 

a = True
b = True
c = False
d = False
# Operador AND
print('Operador AND')
resultado = a and b
print(f'{a} and {b} = {resultado}')
resultado = a and c
print(f'{a} and {c} = {resultado}')

# Operador OR
print('Operador OR')
resultado = a or b
print(f'{a} or {b} = {resultado}')

resultado = a or c
print(f'{a} or {c} = {resultado}')

resultado = d or c
print(f'{d} or {c} = {resultado}')

# Operador NOT
print('Operador NOT')
resultado = not a
print(f'{a} not es {resultado}')
resultado = not c
print(f'{c} not es {resultado}')