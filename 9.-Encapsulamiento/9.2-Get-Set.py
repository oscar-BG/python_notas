# Encapsulamiento, no modificar los atributos directamente

class Persona:
    # Una referencia al objeto que se va a crear 
    def __init__(self, nombre, apellido, edad):
        # Atributos de instancias
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # Método GET
    @property
    def nombre(self):
        print('Llamando metodo get nombre')
        return self._nombre
    
    # Método SET
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre
    # Método de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


# print(type(Persona))
persona1 = Persona('Oscar', 'Bautista', 23)
# Acceder al metodo GET
print(persona1.nombre)

# Cambiar el valor por el metodo set
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)