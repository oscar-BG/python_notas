import psycopg2

conexion = psycopg2.connect(user='director', password='root',host='localhost',port='5002',database='aula_virtual')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # %s : parametro pocisional
            sentencia = "SELECT * FROM materias WHERE id IN %s"
            # llaves_primarias = ((1,2,3))

            entrada = input('Proporciona los id\'ds a buscar (Separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),) 
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()

            for registro in registros:
                print(registro)
            
except Exception as e:
    print(f'Error db {e}')
finally:
    print(f'Close db')
    conexion.close()