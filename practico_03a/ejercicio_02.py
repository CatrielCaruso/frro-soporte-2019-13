# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

from sqlalchemy.orm import sessionmaker
import datetime
from practico_03a.ejercicio_01 import reset_tabla, Persona, engine

DBSession = sessionmaker (bind = engine)
session = DBSession()

def agregar_persona(nombre, nacimiento, dni, altura):
    per = Persona()
    per.nombre=nombre
    per.fechaNacimiento=nacimiento
    per.dni=dni
    per.altura = altura

    session.add(per)
    session.commit()
    result = session.query(Persona).order_by(Persona.idPersona.desc()).first()
    return result.idPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
 pruebas()