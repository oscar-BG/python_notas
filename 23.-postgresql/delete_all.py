import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM materias WHERE id IN %s"
            entrada = input('Ingresa el id de la materia a eliminar (Separado por comas): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados:  {registros_eliminados}')
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()