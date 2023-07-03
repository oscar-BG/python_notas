class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadora_str = ''
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()

        return f'''
            Orden: {self._id_orden}
            Computadora: {computadora_str}
        '''