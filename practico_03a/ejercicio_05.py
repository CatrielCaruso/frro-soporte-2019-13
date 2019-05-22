# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from practico_03a.ejercicio_01 import reset_tabla, Persona, engine
from practico_03a.ejercicio_02 import agregar_persona
from practico_03a.ejercicio_04 import buscar_persona

DBSession = sessionmaker(bind = engine)
session = DBSession()

def actualizar_persona(id_persona, nom, nacimiento, doc, alt):
    busq = buscar_persona(id_persona)

    if (busq):
        enc = session.query(Persona).filter(Persona.idPersona == id_persona).first()
        enc.nombre = nom
        enc.fechaNacimiento = nacimiento
        enc.dni = doc
        enc.altura = alt
        session.commit()
        return True
    return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181) is True
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
 pruebas()