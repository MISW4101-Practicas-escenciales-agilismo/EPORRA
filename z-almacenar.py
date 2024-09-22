from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apostador import Apostador
from src.modelo.apuesta import Apuesta
from src.modelo.ganancia import Ganancia
from src.modelo.declarative_base import Session, engine, Base
from pathlib import Path
import os

my_file = Path("aplicacion.sqlite")
if my_file.is_file():
   os.remove("aplicacion.sqlite")

if __name__ == '__main__':
   #Crea la BD
   Base.metadata.create_all(engine)

   #Abre la sesión
   session = Session()

   ##############################################################################
   apostador1 = Apostador(Nombre = "Pepe Pérez")
   session.add(apostador1)
   apostador2 = Apostador(Nombre = "Ana Andrade")
   session.add(apostador2)
   apostador3 = Apostador(Nombre = "Aymara Castillo")
   session.add(apostador3)
   ##############################################################################
   carrera1 = Carrera(Nombre = "Formula 2", Abierta = True)
   session.add(carrera1)

   competidor_1_1 = Competidor(Nombre = "Juan Pablo Montoya", Probabilidad = 0.15)
   session.add(competidor_1_1)
   competidor_1_2 = Competidor(Nombre = "Kimi Räikkönen", Probabilidad = 0.2)
   session.add(competidor_1_2)
   competidor_1_3 = Competidor(Nombre = "Michael Schumacher", Probabilidad = 0.65)
   session.add(competidor_1_3)

   carrera1.Competidores = [competidor_1_1, competidor_1_2, competidor_1_3]
   ##############################################################################
   carrera2 = Carrera(Nombre = "Atletismo 100 m planos", Abierta = True)
   session.add(carrera2)

   competidor_2_1 = Competidor(Nombre = "Usain Bolt", Probabilidad = 0.72)
   session.add(competidor_2_1)
   competidor_2_2 = Competidor(Nombre = "Lamont Marcell Jacobs", Probabilidad = 0.13)
   session.add(competidor_2_2)
   competidor_2_3 = Competidor(Nombre = "Su Bingtian", Probabilidad = 0.05)
   session.add(competidor_2_3)
   competidor_2_4 = Competidor(Nombre = "Robson da Silva", Probabilidad = 0.1)
   session.add(competidor_2_4)

   carrera2.Competidores = [competidor_2_1, competidor_2_2, competidor_2_3, competidor_2_4]
   ##############################################################################
   apuesta0 = Apuesta(Apostador = "Pepe Pérez", Carrera = "Atletismo 100 m planos", Valor = 10, Competidor = "Usain Bolt")
   session.add(apuesta0)
   apuesta1 = Apuesta(Apostador = "Pepe Pérez", Carrera = "Formula 2", Valor = 10, Competidor = "Juan Pablo Montoya")
   session.add(apuesta1)
   apuesta2 = Apuesta(Apostador = "Ana Andrade", Carrera = "Formula 2", Valor = 25, Competidor = "Michael Schumacher")
   session.add(apuesta2)
   apuesta3 = Apuesta(Apostador = "Aymara Castillo", Carrera = "Formula 2", Valor = 14, Competidor = "Juan Pablo Montoya")
   session.add(apuesta3)
   apuesta4 = Apuesta(Apostador = "Aymara Castillo", Carrera = "Atletismo 100 m planos", Valor = 45, Competidor = "Su Bingtian")
   session.add(apuesta4)

   carrera1.Apuestas = [apuesta1, apuesta2, apuesta3]
   carrera2.Apuestas = [apuesta0, apuesta4]

   apostador1.Apuestas = [apuesta0, apuesta1]
   apostador2.Apuestas = [apuesta2]
   apostador3.Apuestas = [apuesta3, apuesta4]

   competidor_1_1.Apuestas = [apuesta1, apuesta3]
   competidor_1_2.Apuestas = []
   competidor_1_3.Apuestas = [apuesta2]

   competidor_2_1.Apuestas = [apuesta0]
   competidor_2_2.Apuestas = []
   competidor_2_3.Apuestas = [apuesta4]
   competidor_2_4.Apuestas = []
 ##############################################################################

   ganancia_1_1 = Ganancia(Carrera = "Formula 2", Apostador = "Pepe Pérez", Valor = 13)
   session.add(ganancia_1_1)
   ganancia_1_2 = Ganancia(Carrera = "Formula 2", Apostador = "Ana Andrade", Valor = 0)
   session.add(ganancia_1_2)
   ganancia_1_3 = Ganancia(Carrera = "Formula 2", Apostador = "Aymara Castillo", Valor = 15)
   session.add(ganancia_1_3)

   carrera1.Ganancias = [ganancia_1_1, ganancia_1_2, ganancia_1_3]
   carrera1.GananciasCasa = 4

   ganancia_2_1 = Ganancia(Carrera = "Atletismo 100 m planos", Apostador = "Pepe Pérez", Valor = 32)
   session.add(ganancia_1_1)
   ganancia_2_2 = Ganancia(Carrera = "Atletismo 100 m planos", Apostador = "Ana Andrade", Valor = 12)
   session.add(ganancia_1_2)
   ganancia_2_3 = Ganancia(Carrera = "Atletismo 100 m planos", Apostador = "Aymara Castillo", Valor = 34)
   session.add(ganancia_1_3)

   carrera2.Ganancias = [ganancia_2_1, ganancia_2_2, ganancia_2_3]
   carrera2.GananciasCasa = -10
   ##############################################################################
   session.commit()
   session.close()
