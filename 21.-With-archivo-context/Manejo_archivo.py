class ManejoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Estamos entrando al recuros'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_exception, traza_error):
        print('Cerramos el recuros'.center(50, '-'))
        if self.nombre:
            self.nombre.close()