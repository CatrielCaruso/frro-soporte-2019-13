# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import reset_tabla, engine, Persona
from practico_03a.ejercicio_02 import agregar_persona

DBSession = sessionmaker(bind=engine)
session = DBSession()

def buscar_persona(id_persona):
    busq = session.query(Persona).filter(Persona.idPersona == id_persona).first()

    if busq != None:
        return busq.idPersona, busq.nombre, busq.fechaNacimiento, busq.dni, busq.altura
    else:
        return False



@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
 pruebas()