# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///mibase.db')

class Persona(Base):
    __tablename__ = 'personas'
    idPersona = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    dni = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)

def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper