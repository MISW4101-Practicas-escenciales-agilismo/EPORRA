from src.logica.Fachada_EPorra import Fachada_EPorra
from src.modelo.carrera import Carrera
from src.modelo.apostador import Apostador
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta
from src.modelo.ganancia import Ganancia
from src.modelo.declarative_base import Session, engine, Base


class Logica_mock(Fachada_EPorra):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.carreras = []
        self.apostadores = []
        self.ganancias = []
        
############################CARERRAS############################    
    def crear_carrera(self, nombre):
        carrera = Carrera(Nombre = nombre, Abierta = True)
        self.session.add(carrera)
        #self.carreras.append(carrera)
        self.session.commit()

    def dar_carreras(self):
        self.carreras = self.session.query(Carrera).all()
        carrerasDICT = [{'Nombre': carrera.Nombre, 'Competidores': [carrera.Competidores], 'Apuestas': [carrera.Apuestas], 'Abierta': carrera.Abierta} for carrera in self.carreras]
        return carrerasDICT
    
    def dar_carrera(self, id_carrera):
        carrera = self.carreras[id_carrera]
        carreraDICT = {'Nombre': carrera.Nombre, 'Competidores': [carrera.Competidores], 'Apuestas': [carrera.Apuestas], 'Abierta': carrera.Abierta}
        return carreraDICT
    
    def editar_carrera(self, id_carrera, nombre):
        carrera = self.carreras[id_carrera]        
        carrera.Nombre = nombre
        self.session.commit()

    def validar_crear_editar_carrera(self, nombre, competidores):
        if (nombre != "" and len(competidores)>0):
            return ""
        else:
            return "Para guardar una carrera, esta debe tener nombre y por lo menos 1 competidor"
        
    def eliminar_carrera(self, id):
        carrera = self.carreras[id]
        self.session.delete(carrera)
        self.session.commit()    
        
    def terminar_carrera(self, id, ganador):
        print(ganador)
        carrera = self.carreras[id]
        carrera.Ganador = ganador
        self.session.add(carrera)
        self.session.commit()
        self.ganancias = self.session.query(Ganancia).all()

    def dar_reporte_ganancias(self, id_carrera, id_competidor):
        carrera = self.carreras[id_carrera]
        carrera.Abierta=False
        self.session.add(carrera)
        self.session.commit()

            
        for ganancias in self.ganancias:
            return ganancias.Ganancia, ganancias.GananciasCasa

###################################################################
############################COMPETIDORES############################
    def aniadir_competidor(self, id, nombre, probabilidad):
        competidor = Competidor(Nombre = nombre, Probabilidad = probabilidad)
        self.carreras[id].Competidores.append(competidor)
        self.session.commit()

    def dar_competidores_carrera(self, id):
        competidores = self.carreras[id].Competidores
        return [{'Nombre': competidor.Nombre, 'Probabilidad': competidor.Probabilidad} for competidor in competidores]
    
    def dar_competidor(self, id_carrera, id_competidor):
        competidor = self.carreras[id_carrera].Competidores[id_competidor]
        return competidor

    def editar_competidor(self, id_carrera, id_competidor, nombre, probabilidad):
        self.carreras[id_carrera].Competidores[id_competidor].Nombre = nombre
        self.carreras[id_carrera].Competidores[id_competidor].Probabilidad = probabilidad
        self.session.commit()

    def eliminar_competidor(self, id_carrera, id_competidor):
        competidor = self.carreras[id_carrera].Competidores[id_competidor]
        self.session.delete(competidor)
        self.session.commit()    
###################################################################
############################APOSTADORES############################
    def aniadir_apostador(self, nombre):
        self.session.add(Apostador(Nombre = nombre))
        self.session.commit()

    def dar_apostadores(self):
        self.apostadores = self.session.query(Apostador).all()
        apostadoresDICT = [{'Nombre': apostador.Nombre, 'Apuestas': [apostador.Apuestas]} for apostador in self.apostadores]
        return apostadoresDICT
    
    def editar_apostador(self, id, nombre):
        apostador = self.apostadores[id]
        apostador.Nombre = nombre
        self.session.add(apostador)
        self.session.commit()    

    def validar_crear_editar_apostador(self, nombre):
        if nombre != "":
            return ""
        else:
            return "El nombre del apostador no puede estar vacio"

    def eliminar_apostador(self, id):
        apostador = self.apostadores[id]
        self.session.delete(apostador)
        self.session.commit()    
###################################################################
############################APUESTAS############################
    def crear_apuesta(self, apostador, id_carrera, valor, competidor):
        carrera = self.carreras[id_carrera]
        apuesta = Apuesta(Apostador = apostador, Carrera = carrera.Nombre, Valor = valor, Competidor = competidor)
        self.session.add(apuesta)
        self.session.commit()

    def dar_apuestas_carrera(self, id_carrera):
        apuestas = self.carreras[id_carrera].Apuestas
        return [{'Apostador': apuesta.Apostador, 'Carrera': apuesta.Carrera, 'Valor': apuesta.Valor, 'Competidor': apuesta.Competidor} for apuesta in apuestas]
    
    def dar_apuesta(self, id_carrera, id_apuesta):
        apuesta = self.carreras[id_carrera].Apuestas[id_apuesta]
        return {'Apostador': apuesta.Apostador, 'Carrera': apuesta.Carrera, 'Valor': apuesta.Valor, 'Competidor': apuesta.Competidor}
    
    def eliminar_apuesta(self, id_carrera, id_apuesta):
        apuesta = self.carreras[id_carrera].Apuestas[id_apuesta]
        self.session.delete(apuesta)
        self.session.commit()
    
    def editar_apuesta(self, id_apuesta, apostador, id_carrera, valor, competidor):
        carrera = self.carreras[id_carrera]
        apuesta = carrera.Apuestas[id_apuesta]
        apuesta.Apostador = apostador
        apuesta.Carrera = carrera.Nombre 
        apuesta.Valor = valor
        apuesta.Competidor = competidor
        self.session.add(apuesta)
        self.session.commit()

    def validar_crear_editar_apuesta(self, apostador, carrera, valor, competidor):
        if 1==2:
            return("Error en los valores")
        return ""
################################################################### 
