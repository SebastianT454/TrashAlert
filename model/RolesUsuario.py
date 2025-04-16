from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

"""INSTRUCCIONES:
cambiar el nombre de la clase por el de tu entidad, poner el nombre de la tabla en tablename.
asignar el tipo de dato segun su columna, String para varchar, Integer para int, DateTime para timestamp, LargeBinary para bytea"""

class RolesUsuario(Base):
    __tablename__ = "roles_usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

