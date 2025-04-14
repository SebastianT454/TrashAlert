from model import RolesUsuario
from repository.connector.Connector import SessionLocal

"""
INSTRUCCIONES:
Cambiar todo lo que diga Sector, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga sector, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: RolesUsuario
# nombre variable: rolesUsuario

class RolesUsuarioRepository:

    def save(self,rolesUsuario):
        with SessionLocal() as session:
            session.add(rolesUsuario)
            session.commit()
            rolesUsuario = session.query(RolesUsuario).filter(RolesUsuario.id == rolesUsuario.id).first()
            rolesUsuario.__delattr__('_sa_instance_state')
            return rolesUsuario

    def delete(self,id):
        with SessionLocal() as session:
            session.query(RolesUsuario).filter(RolesUsuario.id == id).delete()
            session.commit()
            return id

    def update(self,rolesUsuario2):
        rolesUsuario2.__delattr__('_sa_instance_state')
        with SessionLocal() as session:
            rolesUsuario = session.query(RolesUsuario).filter(RolesUsuario.id == rolesUsuario2.id).first()

            for key, value in rolesUsuario2.__dict__.items():
                    setattr(rolesUsuario, key, value)
            session.commit()

            rolesUsuario = session.query(RolesUsuario).filter(RolesUsuario.id == rolesUsuario.id).first()
            rolesUsuario.__delattr__('_sa_instance_state')
            return rolesUsuario


    def getId(self,id):
        with SessionLocal() as session:
            rolesUsuario = session.query(RolesUsuario).filter(RolesUsuario.id == id).first()
            rolesUsuario.__delattr__('_sa_instance_state')
            return rolesUsuario

    def getAll(self):
        with SessionLocal() as session:
            lista = session.query(RolesUsuario).all()
            for i in lista:
                i.__delattr__('_sa_instance_state')
            return lista