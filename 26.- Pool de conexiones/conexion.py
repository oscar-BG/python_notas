from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'fixp'
    _USERNAME= 'applab'
    _PASSWORD = 'Applab2022.'
    _DB_PORT = '5001'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:

                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host = cls._HOST, user= cls._USERNAME, password = cls._PASSWORD, port = cls._DB_PORT, database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')

                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
        
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)

    conexion2 = Conexion.obtenerConexion()
    #conexion3 = Conexion.obtenerConexion()
    #conexion4 = Conexion.obtenerConexion()
    #conexion5 = Conexion.obtenerConexion()
    #conexion6 = Conexion.obtenerConexion()