from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

"""INSTRUCCIONES:
cambiar el nombre de la clase por el de tu entidad, poner el nombre de la tabla en tablename.
asignar el tipo de dato segun su columna, String para varchar, Integer para int"""

class EstadosReporte(Base):
    __tablename__ = "estados_reporte"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    
