# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import Persona, engine
from practico_03a.ejercicio_04 import buscar_persona
from practico_03a.ejercicio_02 import agregar_persona
from practico_03a.ejercicio_06 import reset_tabla, Peso

DBSession = sessionmaker(bind=engine)
session = DBSession()

def agregar_peso(id_persona, fecha, peso):
    busq = buscar_persona(id_persona)

    if busq != None:
        enc = session.query(Peso).filter(Peso.idPersona== id_persona and Peso.fecha > fecha).all()
        if enc == []:
            pes = Peso()
            pes.idPersona = id_persona
            pes.fecha = fecha
            pes.peso = peso
            session.add(pes)
            session.commit()

            result = session.query(Peso).filter(Peso.idPersona == id_persona).order_by(Peso.idPeso.desc()).first()
            return result.idPeso
        return False
    return False




@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.date(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018, 5, 16), 80) == False

if __name__ == '__main__':
 pruebas()