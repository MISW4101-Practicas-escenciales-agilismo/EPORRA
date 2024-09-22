from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Apuesta(Base):

    __tablename__ = 'apuesta'
    ID = Column(Integer, primary_key=True)
    Apostador = Column(String, ForeignKey('apostador.Nombre'))
    Carrera = Column(String, ForeignKey('carrera.Nombre'))
    Valor = Column(Integer)
    Competidor = Column(String, ForeignKey('competidor.Nombre'))
    