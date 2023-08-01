import psycopg2 as bd

conexion = bd.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:

    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO materias (nombre, descripcion, activo) VALUES(%s, %s, %s)'
            valores = ('Geografia','1', 'true')
            cursor.execute(sentencia, valores)

            sentencia = "UPDATE materias SET descripcion=%s WHERE id=%s"
            valores = ('1',3)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()

print('Termine la transaccion')