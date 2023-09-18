from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool
class PersonaDAO:
    '''
    DAO (DATA ACCESS OBJECT)
    CRUD (CREATE-READ-UPDATE-DELETE)
    '''

    _SELECCIONAR    = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR       = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR     = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR       = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)

            registros = cursor.fetchall()
            personas= []

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
        
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertar: {persona}')
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizar: {persona}')
            return cursor.rowcount
            

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
            
if __name__== '__main__':

    # Insertar un registros
    persona1 = Persona(nombre='Roko', apellido='Lopez', email='roko@gmail.com')
    personas_agregadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_agregadas}')

    # Actualizar un registro
    persona1 = Persona(1,'Efrain', 'Bautista', 'efra@gmail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro
    persona1 = Persona(id_persona=4)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)