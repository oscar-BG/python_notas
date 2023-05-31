from  Cuadrado  import *
from Rectangulo import *
from FiguraGeometrica import *

# No se puede instanciar  una clase abstracta
#figura1 = FiguraGeomatrica(10, 12)

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calcular área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)


rectangulo1 = Rectangulo(10, 15, 'cafe')
print(f'Calculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)