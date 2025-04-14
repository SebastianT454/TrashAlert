from flask import Blueprint, request
from service import UsuarioService

"""
INSTRUCCIONES:
Cambiar todo lo que diga Usuario, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga usuario, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Usuario
# nombre variable: usuario


# Definir el Blueprint
usuario = Blueprint('usuario', __name__)
usuarioService = UsuarioService()

@usuario.route('/getAll', methods=['GET'])
def getAll():
    return usuarioService.getAll()

@usuario.route('/getid/<int:id>', methods=['GET'])
def getid(id):
    return usuarioService.getId(id)

@usuario.route('/save', methods=['POST'])
def save():
    return usuarioService.save(request.get_json())

@usuario.route('/update', methods=['PUT'])
def update():
    return usuarioService.update(request.get_json())

@usuario.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return usuarioService.delete(id)
