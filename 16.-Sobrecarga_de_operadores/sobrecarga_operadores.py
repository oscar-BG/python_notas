class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self, other):
        return self.nombre + other
    

persona1 = Persona('Juan')
persona2 = Persona('Carlos')

print(persona1 + persona2)
