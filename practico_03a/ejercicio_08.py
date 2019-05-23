# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import engine
from practico_03a.ejercicio_04 import buscar_persona
from practico_03a.ejercicio_02 import agregar_persona
from practico_03a.ejercicio_06 import reset_tabla, Peso
from practico_03a.ejercicio_07 import agregar_peso

DBSession = sessionmaker(bind=engine)
session = DBSession()

def listar_pesos(id_persona):
    busq = buscar_persona(id_persona)
    if busq != False:
        enc = session.query(Peso.peso, Peso.fecha).filter(Peso.idPersona == id_persona).all()
        return False if enc is None else enc
    else:
        return False





@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.date(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.date(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
 pruebas()