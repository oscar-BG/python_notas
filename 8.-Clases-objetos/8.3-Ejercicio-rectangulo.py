class CalcularBase():
    def __init__(self, base, alruta):
        self.base = base
        self.altura = alruta

    def calcular_area(self):
        return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Propociona la altura: '))

rectagulo1 = CalcularBase(base,altura)
print(rectagulo1.calcular_area())