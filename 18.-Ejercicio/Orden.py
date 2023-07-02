class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)

    @property
    def id_orden(self):
        return self._id_orden
    
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        for computadora in self._computadoras:
            print(computadora)


orden1 = Orden()