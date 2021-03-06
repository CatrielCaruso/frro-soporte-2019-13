# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    db = sqlite3.connect('mibase')
    cur = db.cursor()
    cur.execute('SELECT fecha from PersonaPeso where idPersona=?', (id_persona,))
    per = cur.fetchall()
    b = 0
    if per != None:
        for i in per:
            aux = datetime.datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
            i_1 = aux.date()
            if i_1 > fecha.date():
                    b = 1
                    break


    if b == 0:
        if buscar_persona(id_persona) != False:
                cSQL = 'INSERT into PersonaPeso (idPersona, fecha, peso) VALUES (?,?,?)'
                tdatos = (id_persona, fecha, peso )
                cur.execute(cSQL, tdatos)
                cur.close()
                db.commit()
                db.close()
                return id_persona
        return False
    return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez',datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    #id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    #registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__== '___main___':
    pruebas()
