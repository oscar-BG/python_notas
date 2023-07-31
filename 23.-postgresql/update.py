import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE materias SET nombre=%s WHERE id=%s"

            valores = (('Quimica cuantica', 1),
                       ('Historia mexico', 6),
                       ('Matematicas', 3),
                       )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados:  {registros_actualizados}')
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()