from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

"""INSTRUCCIONES:
cambiar el nombre de la clase por el de tu entidad, poner el nombre de la tabla en tablename.
asignar el tipo de dato segun su columna, String para varchar, Integer para int, DateTime para timestamp, LargeBinary para bytea"""

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    password = Column(String)
    id_rol = Column(Integer)
    
