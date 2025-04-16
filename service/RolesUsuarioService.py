import json

from model import RolesUsuario
from repository.postgres.RolesUsuarioRepository import RolesUsuarioRepository

"""
INSTRUCCIONES:
Cambiar todo lo que diga RolesUsuario, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga rolesUsuario, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: RolesUsuario
# nombre variable: rolesUsuario

class RolesUsuarioService:

    def __init__(self):
        self.repository = RolesUsuarioRepository()


    def save(self, rolesUsuario):
        obj = RolesUsuario()
        for key, value in rolesUsuario.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.save(obj)))


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, rolesUsuario):
        obj = RolesUsuario()
        for key, value in rolesUsuario.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        return json.dumps(vars(self.repository.getId(id)))

    def getAll(self):
        data = [json.dumps(vars(objeto)) for objeto in self.repository.getAll()]
        parsed_data = [json.loads(item) for item in data]
        return json.dumps(parsed_data, indent=4)