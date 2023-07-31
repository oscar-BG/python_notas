import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM materias"
            cursor.execute(sentencia)
            # fetchall: optiene todos los registros de la consulta
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()