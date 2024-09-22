from src.modelo.carrera import Carrera
from src.modelo.apostador import Apostador
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta
from src.modelo.declarative_base import Session, engine, Base


if __name__ == '__main__':
    session = Session()
    carreras = session.query(Carrera).all()
    print("Carreras:")
    for carrera in carreras:
        print(f"---{carrera.Nombre}")
        print("------Competidores:")
        for competidor in carrera.Competidores:
            print(f"---------|Nombre: {competidor.Nombre} |Probabilidad: {str(competidor.Probabilidad)}")
       
    apostadores = session.query(Apostador).all()
    print("Apostadores:")
    for apostador in apostadores:
        print(f"---Apostador: {apostador.Nombre}")

    print("Apuestas:")
    apuestas = session.query(Apuesta).all()
    for apuesta in apuestas:
        print(f"---|Apostador: {apuesta.Apostador}|Carrera: {apuesta.Carrera}|Valor: {str(apuesta.Valor)}|Competidor: {apuesta.Competidor}")


session.close()