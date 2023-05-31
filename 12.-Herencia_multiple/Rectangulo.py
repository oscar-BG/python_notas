from FiguraGeometrica import *
from Color import *

class Rectangulo(FiguraGeomatrica, Color):

    def __init__(self, ancho, alto, color):
        FiguraGeomatrica.__init__(self, ancho, alto)
        Color.__init__(self,  color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f'{FiguraGeomatrica.__str__(self)} {Color.__str__(self)}'
    
