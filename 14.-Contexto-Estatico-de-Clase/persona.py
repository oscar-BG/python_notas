class Persona:
    contador_persona = 0

    @classmethod
    def generar_id(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_id()
        self.nombre     = nombre
        self.edad       = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]' 
    

persona1 = Persona('Javier', 50)
print(f'Persona 1: {persona1}')

persona2 = Persona('Eduardo', 20)
print(f'Persona 2: {persona2}')

print(f'Contador persona: {Persona.contador_persona}')