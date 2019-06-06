# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy import Column, Integer, Date, ForeignKey
from practico_03a.ejercicio_01 import borrar_tabla, crear_tabla, Base, engine

class Peso(Base):
    __tablename__ = 'tabla_peso'
    idPeso = Column(Integer, primary_key=True)
    idPersona = Column(Integer, ForeignKey('personas.idPersona'))
    fecha = Column(Date, nullable=False)
    peso = Column(Integer, nullable=False)

def crear_tabla_peso():
    Base.metadata.create_all(engine)



def borrar_tabla_peso():
    Peso.__table__.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper