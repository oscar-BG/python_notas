class Persona:
    # Una referencia al objeto que se va a crear 
    def __init__(self, nombre, apellido, edad, *agrgs, **kwargs):
        # Atributos de instancias
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = agrgs
        self.terminos = kwargs
    
    # Método de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


# print(type(Persona))
persona1 = Persona('Oscar', 'Bautista', 23, '4456754567', 2, 3, 5, m='manzana', p='pera') 
persona1.mostrar_detalle()
# Atributos de instancia
persona1.telefono = '5545678546'
print(f'Telefono: {persona1.telefono}')
persona2 = Persona('Laura', 'Jimenez', 40)
persona2.mostrar_detalle()