# Funciones en Python
# Agregar valores por default a las funciones

# Iniciarmos un valor por default si no enviarmos parametros
def sumar(a = 0,b = 0):
    # Regresa el valor de la suma
    return a + b 

print(f"Si no pasamos argumentos {sumar()}")
resultado = sumar(5,6)
print(resultado)
