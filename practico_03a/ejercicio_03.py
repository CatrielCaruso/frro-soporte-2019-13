# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import reset_tabla, Persona, engine
from practico_03a.ejercicio_02 import agregar_persona

Session = sessionmaker(bind = engine)
session = Session()

def borrar_persona(id_persona):
    busq = session.query(Persona).filter(Persona.idPersona==id_persona).delete()
    session.commit()
    if(busq):
        return True
    return False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
 pruebas()