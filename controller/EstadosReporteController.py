from flask import Blueprint, request
from service import EstadosReporteService

"""
INSTRUCCIONES:
Cambiar todo lo que diga EstadosReporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga estadosReporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: EstadosReporte
# nombre variable: estadosReporte


# Definir el Blueprint
estadosReporte = Blueprint('estadosReporte', __name__)
estadosReporteService = EstadosReporteService()

@estadosReporte.route('/getAll', methods=['GET'])
def getAll():
    return estadosReporteService.getAll()

@estadosReporte.route('/getid/<int:id>', methods=['GET'])
def getid(id):
    return estadosReporteService.getId(id)

@estadosReporte.route('/save', methods=['POST'])
def save():
    return estadosReporteService.save(request.get_json())

@estadosReporte.route('/update', methods=['PUT'])
def update():
    return estadosReporteService.update(request.get_json())

@estadosReporte.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return estadosReporteService.delete(id)
