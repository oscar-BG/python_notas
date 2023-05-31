def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f' {llave} : {valor}')

listarTerminos(IDE='Desarrollo', PK='Llave primaria')