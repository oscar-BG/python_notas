from computadora import *
from dispositivo_entrada import *
from monitor import *
from orden import *
from raton import *
from teclado import *

teclado1 = Teclado('HP', 'UBS')
raton1 = Raton('HP', 'UBS')
monitor1 = Monitor('HP', 20)

computadora1 = Computadora('HP', monitor1, teclado1, raton1)
#print(computadora1)


teclado2 = Teclado('Gamer', 'Blueetooth')
raton1 = Raton('HP', 'USB')
monitor2 = Monitor('Acer', 20)

computadora2 = Computadora('Acer', monitor2, teclado2, raton1)
#print(computadora2)

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 34)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)
