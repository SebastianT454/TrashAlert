from flask import Blueprint, request
from service import RolesUsuarioService

"""
INSTRUCCIONES:
Cambiar todo lo que diga RolesUsuario, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga rolesUsuario, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: RolesUsuario
# nombre variable: rolesUsuario


# Definir el Blueprint
rolesUsuario = Blueprint('rolesUsuario', __name__)
rolesUsuarioService = RolesUsuarioService()

@rolesUsuario.route('/getAll', methods=['GET'])
def getAll():
    return rolesUsuarioService.getAll()

@rolesUsuario.route('/getid/<int:id>', methods=['GET'])
def getid(id):
    return rolesUsuarioService.getId(id)

@rolesUsuario.route('/save', methods=['POST'])
def save():
    return rolesUsuarioService.save(request.get_json())

@rolesUsuario.route('/update', methods=['PUT'])
def update():
    return rolesUsuarioService.update(request.get_json())

@rolesUsuario.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return rolesUsuarioService.delete(id)
