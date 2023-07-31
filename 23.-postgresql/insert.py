import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO materias (nombre, descripcion, activo) VALUES(%s, %s, %s)'
            valores = ('Fisica','Grado 1', 'false')
            cursor.execute(sentencia, valores)

            # conexion.commit : guarda los cambios en la base de datos, pero al usar el with no es necesario
            registros_insertados = cursor.rowcount
            print(f'Registros insertados {registros_insertados}')
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()