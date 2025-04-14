from sqlalchemy import Column, Integer, String
from repository.connector.Connector import Base

class RolesUsuario(Base):
    __tablename__ = "roles_usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

