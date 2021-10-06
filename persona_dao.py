from logger_base import log
from persona import Persona

from conexion import Conexion


class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre =%s, apellido =%s, email =%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona eliminada: {persona}')
                return cursor.rowcount


if __name__ == '__main__':

    # insertar un registro
    # persona1 = Persona(nombre='Pedro', apellido='Gomez', email='pgomez@mail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Persona insertada: {personas_insertadas} ')
    # actualizar un registro
    # persona1 = Persona(id_persona=4,nombre='Carlos', apellido='Jimenez', email='cjimenez@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Persona actualizada: {personas_actualizadas} ')
    # eliminar un registro
    persona1 = Persona(id_persona=8)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Persona eliminada: {personas_eliminadas} ')
    # listar registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
