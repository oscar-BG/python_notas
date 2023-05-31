"""
Ejercicio: Comvertidor de temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""
def celsius_fahrenheit(celsius):
    return (celsius * 9) / 5 +32

def fahrenheit_celsius(fah):
    return ((fah-32) * 5) / 9


####

celsius = float(input("Proporcione valor en celsius: ")) 
resultado = celsius_fahrenheit(celsius)

print(f'{celsius} C a F: {resultado:.2f}')

fahre = float(input("Propociones valor en fah: ")) 
resultado = fahrenheit_celsius(fahre)

print(f'{fahre} F a C: {resultado:.2f}')