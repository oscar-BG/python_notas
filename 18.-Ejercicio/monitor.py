class Monitor:
    contador_monitores = 0

    def __init__(self, marca, plugadas):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._plugadas = plugadas

    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, plugadas: {self._plugadas}'
    

if __name__ == '__main__':
    monitor1 = Monitor('HP', '16')
    print(f'Monitor 1: {monitor1}')

    monitor2 = Monitor('Acer', 20)
    print(f'Monitor 2: {monitor2}')

