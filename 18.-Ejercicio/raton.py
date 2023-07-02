from dispositivo_entrada import *

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_raton}, Marca: {self._marca}, Tipo entrada: {self._tipo_entrada}'
    

if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(f'Raton 1 {raton1}')

    raton2 = Raton('Acer', 'Bluetooh')
    print(f'Raton 2 {raton2}')