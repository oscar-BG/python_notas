# Importar modulo
from Persona import Persona


print('Creación objetos'.center(50,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

# Nombre del modulo
print(__name__) 

print('Eliminación objetos'.center(50,'-'))