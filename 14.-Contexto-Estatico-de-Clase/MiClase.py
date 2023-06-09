class MiClase:

    # Su valor es compartida por todos los objetos
    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        # Las variables de instancias tiene un valor por cada objeto creado de la clase
        self.variables_instancia = variable_instancia

    # Metodo estatico asociado a la clase
    @staticmethod
    def metodo_estatico():
        # Acceder a la variable de clase
        print(MiClase.variables_clase)

    # Método de clase
    @classmethod
    def metodo_clase(cls):
        #Recibe el cls que hacer referencia a la clase
        print(f'Método de clase: {cls.variables_clase}')
    

print(MiClase.variables_clase)

miObjeto1 = MiClase('Objeto 1')
print(f' Objeto 1 Variable de clase: {miObjeto1.variables_clase}')
print(f' Objeto 1 Variable de instancia: {miObjeto1.variables_instancia}')


miObjeto2 = MiClase('Objeto 2')
print(f'Objeto 2 Variable de clase: {miObjeto2.variables_clase}')
print(f'Objeto 2 Variable de instancia: {miObjeto2.variables_instancia}')


#  ************* Creación de variables de clase al vuele

# Utilizar La clase para crear variables
MiClase.variables_clase2 = 'Segunda variable'


# Acceder a la nueva variable variables_calse2
print(f'Variable 2 {MiClase.variables_clase2}')
print(f'Variable 2 desde objeto {miObjeto1.variables_clase2}')

# Acceder al método statico
MiClase.metodo_estatico()

# Acceder al método de clase
MiClase.metodo_clase()
miObjeto1.metodo_clase()