from Orden import Orden
from Producto import Producto 


producto1 = Producto('Camisa', 100)
producto2 = Producto('Pantalon', 120)
producto3 = Producto('Calcetines', 50)
producto4 = Producto('Blusa', 60)


productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden2 = Orden(productos2)

orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(orden2)

print(f'Total orden 1 {orden1.calcular_total()}')
print(f'Total orden 2 {orden2.calcular_total()}')