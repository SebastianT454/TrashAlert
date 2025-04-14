from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

class EstadosReporte(Base):
    __tablename__ = "estados_reporte"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    
