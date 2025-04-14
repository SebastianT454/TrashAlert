import json

from model import Usuario
from repository.postgres.UsuarioRepository import UsuarioRepository

"""
INSTRUCCIONES:
Cambiar todo lo que diga Usuario, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga usuario, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Usuario
# nombre variable: usuario

class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()


    def save(self, usuario):
        obj = Usuario()
        for key, value in usuario.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.save(obj)))


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, usuario):
        obj = Usuario()
        for key, value in usuario.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        return json.dumps(vars(self.repository.getId(id)))

    def getAll(self):
        return [json.dumps(vars(objeto)) for objeto in self.repository.getAll()]