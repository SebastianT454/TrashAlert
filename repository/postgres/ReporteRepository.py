from model import Reporte
from repository.connector.Connector import SessionLocal

"""
INSTRUCCIONES:
Cambiar todo lo que diga Sector, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga sector, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Reporte
# nombre variable: reporte

class ReporteRepository:

    def save(self,reporte):
        with SessionLocal() as session:
            session.add(reporte)
            session.commit()
            reporte = session.query(Reporte).filter(Reporte.id == reporte.id).first()
            reporte.__delattr__('_sa_instance_state')
            return reporte

    def delete(self,id):
        with SessionLocal() as session:
            session.query(Reporte).filter(Reporte.id == id).delete()
            session.commit()
            return id

    def update(self,reporte2):
        reporte2.__delattr__('_sa_instance_state')
        with SessionLocal() as session:
            reporte = session.query(Reporte).filter(Reporte.id == reporte2.id).first()

            for key, value in reporte2.__dict__.items():
                    setattr(reporte, key, value)
            session.commit()

            reporte = session.query(Reporte).filter(Reporte.id == reporte.id).first()
            reporte.__delattr__('_sa_instance_state')
            return reporte


    def getId(self,id):
        with SessionLocal() as session:
            reporte = session.query(Reporte).filter(Reporte.id == id).first()
            reporte.__delattr__('_sa_instance_state')
            return reporte

    def getAll(self):
        with SessionLocal() as session:
            lista = session.query(Reporte).all()
            for i in lista:
                i.__delattr__('_sa_instance_state')
            return lista