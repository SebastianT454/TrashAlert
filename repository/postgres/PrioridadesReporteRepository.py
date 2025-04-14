from model import PrioridadesReporte
from repository.connector.Connector import SessionLocal

"""
INSTRUCCIONES:
Cambiar todo lo que diga Sector, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga sector, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: PrioridadesReporte
# nombre variable: prioridadesReporte

class PrioridadesReporteRepository:

    def save(self,prioridadesReporte):
        with SessionLocal() as session:
            session.add(prioridadesReporte)
            session.commit()
            prioridadesReporte = session.query(PrioridadesReporte).filter(PrioridadesReporte.id == prioridadesReporte.id).first()
            prioridadesReporte.__delattr__('_sa_instance_state')
            return prioridadesReporte

    def delete(self,id):
        with SessionLocal() as session:
            session.query(PrioridadesReporte).filter(PrioridadesReporte.id == id).delete()
            session.commit()
            return id

    def update(self,prioridadesReporte2):
        prioridadesReporte2.__delattr__('_sa_instance_state')
        with SessionLocal() as session:
            prioridadesReporte = session.query(PrioridadesReporte).filter(PrioridadesReporte.id == prioridadesReporte2.id).first()

            for key, value in prioridadesReporte2.__dict__.items():
                    setattr(prioridadesReporte, key, value)
            session.commit()

            prioridadesReporte = session.query(PrioridadesReporte).filter(PrioridadesReporte.id == prioridadesReporte.id).first()
            prioridadesReporte.__delattr__('_sa_instance_state')
            return prioridadesReporte


    def getId(self,id):
        with SessionLocal() as session:
            prioridadesReporte = session.query(PrioridadesReporte).filter(PrioridadesReporte.id == id).first()
            prioridadesReporte.__delattr__('_sa_instance_state')
            return prioridadesReporte

    def getAll(self):
        with SessionLocal() as session:
            lista = session.query(PrioridadesReporte).all()
            for i in lista:
                i.__delattr__('_sa_instance_state')
            return lista