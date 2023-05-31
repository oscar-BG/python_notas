# Encapsulamiento, no modificar los atributos directamente

class Persona:
    # Una referencia al objeto que se va a crear 
    def __init__(self, nombre, apellido, edad):
        # Atributos de instancias
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # Método de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


# print(type(Persona))
persona1 = Persona('Oscar', 'Bautista', 23) 
persona1._nombre = 'Gabriel' # Puede ser modificado pero no es lo recomendable
persona1.mostrar_detalle()