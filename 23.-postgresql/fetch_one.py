import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # %s : parametro pocisional
            sentencia = "SELECT * FROM materias WHERE id = %s"
            id_materia = input('Proporciona el valor de id materia: ')
            cursor.execute(sentencia, (id_materia,))
            # fetchone: optiene el primer registro de la consulta
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()