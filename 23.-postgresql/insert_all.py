import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO materias (nombre, descripcion, activo) VALUES(%s, %s, %s)'
            valores = (
                ('Algebra','Grado 6', 'true'),
                ('Programación','Grado 4', 'true'),
                ('Historia','Grado 1', 'false'),
                )
            
            # executemany: inserta varios registros
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados {registros_insertados}')
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()