from dispositivo_entrada import *

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_taclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_taclado}, Marca: {self._marca}, Tipo entrada: {self._tipo_entrada}'
    

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(f'Teclado 1: {teclado1}')


    teclado2 = Teclado('Gamer', 'Blueetooth')
    print(f'Teclado 2: {teclado2}')

