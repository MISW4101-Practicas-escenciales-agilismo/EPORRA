from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Carrera(Base):

    __tablename__ = 'carrera'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Abierta = Column(Boolean)
    Competidores = relationship('Competidor', cascade='all, delete, delete-orphan')
    Apuestas = relationship('Apuesta', cascade='all, delete-orphan')
    Ganador = relationship('Competidor', cascade='all, delete, delete-orphan')
    '''
    all : hacer propagación de operaciones cuando se guarda o actualiza información. 
    Por ejemplo, cuando se crea una canción con dos intérpretes, al almacenar la canción se deben almacenar los intérpretes también.
    delete : al momento de borrar un objeto, de manera que los objetos relacionados también se borren.
    Por ejemplo, al borrar una canción se deben borrar sus intérpretes.
    delete-orphan : al momento de desasociar un objeto relacionado, por ejemplo,
    cuando un intérprete deja de hacer parte de una canción, al guardar los cambios el intérprete debe ser borrado.
    '''