# Cuando desconocemos el numero total de argumentos que queremos pasar a una funcion

def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listaNombres('Juan', 'Karla','Maria','Ernesto')