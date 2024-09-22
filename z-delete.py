from src.modelo.apostador import Apostador
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
  session = Session()
  apostador = session.query(Apostador).offset(1).limit(1).first()
  session.delete(apostador)
  session.commit()
  session.close()