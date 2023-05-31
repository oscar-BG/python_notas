class FiguraGeomatrica:
    def __init__(self, ancho, alto):

        if self._validar_valor_(ancho):
            self._ancho  = ancho
        else:
            self._ancho = 0

        if  self._validar_valor_(alto):
            self._alto   = alto
        else:
            self.alto = 0
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor_(ancho):
            self._ancho = ancho
        else :
            self._ancho = 0

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor_(alto):
            self._alto = alto
        else:
            self._alto = 0

    def __str__(self):
        return f'Alto: {self.alto}, Ancho {self.ancho}'
    
    def _validar_valor_(self, valor):
        return True if 0 < valor < 10 else False