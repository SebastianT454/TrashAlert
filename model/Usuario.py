from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    password = Column(String)
    id_rol = Column(Integer)
    
