from model import Usuario
from repository.connector.Connector import SessionLocal

"""
INSTRUCCIONES:
Cambiar todo lo que diga Sector, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga sector, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Usuario
# nombre variable: usuario

class UsuarioRepository:

    def save(self,usuario):
        with SessionLocal() as session:
            session.add(usuario)
            session.commit()
            usuario = session.query(Usuario).filter(Usuario.id == usuario.id).first()
            usuario.__delattr__('_sa_instance_state')
            return usuario

    def delete(self,id):
        with SessionLocal() as session:
            session.query(Usuario).filter(Usuario.id == id).delete()
            session.commit()
            return id

    def update(self,usuario2):
        usuario2.__delattr__('_sa_instance_state')
        with SessionLocal() as session:
            usuario = session.query(Usuario).filter(Usuario.id == usuario2.id).first()

            for key, value in usuario2.__dict__.items():
                    setattr(usuario, key, value)
            session.commit()

            usuario = session.query(Usuario).filter(Usuario.id == usuario.id).first()
            usuario.__delattr__('_sa_instance_state')
            return usuario


    def getId(self,id):
        with SessionLocal() as session:
            usuario = session.query(Usuario).filter(Usuario.id == id).first()
            usuario.__delattr__('_sa_instance_state')
            return usuario

    def getAll(self):
        with SessionLocal() as session:
            lista = session.query(Usuario).all()
            for i in lista:
                i.__delattr__('_sa_instance_state')
            return lista