class Cubo():
    def __init__(self, alto, ancho, profundo):
        self.alto       = alto
        self.ancho      = ancho
        self.profundo   = profundo
    
    def volumen(self):
        return self.alto * self.ancho * self.profundo
    

alto        = int(input('Propociona el alto: '))
ancho       = int(input('Proporciona el ancho: '))
profundo    = int(input('Proporciona la profundidas'))

cubo1 = Cubo(alto, ancho, profundo)
print(f'Volumen de cubo: {cubo1.volumen()}')