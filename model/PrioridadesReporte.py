from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

class PrioridadesReporte(Base):
    __tablename__ = "prioridades_reporte"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    
