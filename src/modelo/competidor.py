from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Competidor(Base):

    __tablename__ = 'competidor'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Probabilidad = Column(Float)
    Carrera = Column(String, ForeignKey('carrera.Nombre'))
    Apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')