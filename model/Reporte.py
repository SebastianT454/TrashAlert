from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from repository.connector.Connector import Base
 
 
class Reporte(Base):
    __tablename__ = "reporte"

    id = Column(Integer, primary_key=True)
    imagen = Column(LargeBinary)
    descripcion = Column(String)
    ubicacion = Column(String)
    fecha_reporte = Column(DateTime)
    id_estado = Column(Integer)
    id_prioridad = Column(Integer)
    id_usuario = Column(Integer)
    
