print('Proporcione los siguientes datos del libro: ')

nombre = input('Proporcione el nombre: ')
id = int(input('Proporcione en ID: '))
precio = float(input('Proporcione el precio: '))
envioGratuito = bool(input('Indica si el envio es gratuito (True/False): '))

print(f'Nombre {nombre}')
print(f'Id {id}')
print(f'Precio {precio}')
print(f'Envío Gratuito?: {envioGratuito}')


