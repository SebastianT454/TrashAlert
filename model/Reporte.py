from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from repository.connector.Connector import Base
 
"""INSTRUCCIONES:
cambiar el nombre de la clase por el de tu entidad, poner el nombre de la tabla en tablename.
asignar el tipo de dato segun su columna, String para varchar, Integer para int, DateTime para timestamp, LargeBinary para bytea"""

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
    
