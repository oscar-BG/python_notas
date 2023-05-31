# Encapsulamiento, no modificar los atributos directamente

class Persona:
    # Una referencia al objeto que se va a crear 
    def __init__(self, nombre, apellido, edad):
        # Atributos de instancias
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    # Método GET
    @property
    def nombre(self):
        return self._nombre
    
    # Método SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    # Método de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')       
# __main__ es el nombre del modulo
if __name__ == '__main__':
    # print(type(Persona))
    persona1 = Persona('Oscar', 'Bautista', 23)

    persona1.nombre = 'Gabriel'
    persona1.apellido = 'Sandoval'
    persona1.edad = 40

    persona1.mostrar_detalle()

    # Nombre del modulo
    print(__name__)