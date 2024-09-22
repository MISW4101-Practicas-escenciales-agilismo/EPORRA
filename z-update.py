from src.modelo.carrera import Carrera
from src.modelo.declarative_base import Session, engine, Base


if __name__ == '__main__':
  session = Session()
  carrera = session.query(Carrera).get(2)

  carrera.nombre = "daniel"

  session.add(carrera)
  session.commit()
  session.close()