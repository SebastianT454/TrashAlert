from model import EstadosReporte
from repository.connector.Connector import SessionLocal

"""
INSTRUCCIONES:
Cambiar todo lo que diga Sector, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga sector, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: EstadosReporte
# nombre variable: estadosReporte

class EstadosReporteRepository:

    def save(self,estadosReporte):
        with SessionLocal() as session:
            session.add(estadosReporte)
            session.commit()
            estadosReporte = session.query(EstadosReporte).filter(EstadosReporte.id == estadosReporte.id).first()
            estadosReporte.__delattr__('_sa_instance_state')
            return estadosReporte

    def delete(self,id):
        with SessionLocal() as session:
            session.query(EstadosReporte).filter(EstadosReporte.id == id).delete()
            session.commit()
            return id

    def update(self,estadosReporte2):
        estadosReporte2.__delattr__('_sa_instance_state')
        with SessionLocal() as session:
            estadosReporte = session.query(EstadosReporte).filter(EstadosReporte.id == estadosReporte2.id).first()

            for key, value in estadosReporte2.__dict__.items():
                    setattr(estadosReporte, key, value)
            session.commit()

            estadosReporte = session.query(EstadosReporte).filter(EstadosReporte.id == estadosReporte.id).first()
            estadosReporte.__delattr__('_sa_instance_state')
            return estadosReporte


    def getId(self,id):
        with SessionLocal() as session:
            estadosReporte = session.query(EstadosReporte).filter(EstadosReporte.id == id).first()
            estadosReporte.__delattr__('_sa_instance_state')
            return estadosReporte

    def getAll(self):
        with SessionLocal() as session:
            lista = session.query(EstadosReporte).all()
            for i in lista:
                i.__delattr__('_sa_instance_state')
            return lista