import psycopg2 as bd

conexion = bd.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    #Eviamos guardar los cambios automaticamente
    conexion.autocommit = False

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO materias (nombre, descripcion, activo) VALUES(%s, %s, %s)'
    valores = ('Biologia','1', 'true')
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE materias SET descripcion=%s WHERE id=%s"
    valores = ('Materia grado 1',3)
    cursor.execute(sentencia, valores)

    # Guardamos los cambios de manera manual
    conexion.commit()

    print('Termine la transaccion')
except Exception as e:
    # Reveritomos las consultas para que no se guarden si se encontro un error
    conexion.rollback()
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()