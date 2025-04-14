from flask import Blueprint, request
from service import PrioridadesReporteService

"""
INSTRUCCIONES:
Cambiar todo lo que diga PrioridadesReporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga prioridadesReporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: PrioridadesReporte
# nombre variable: prioridadesReporte


# Definir el Blueprint
prioridadesReporte = Blueprint('prioridadesReporte', __name__)
prioridadesReporteService = PrioridadesReporteService()

@prioridadesReporte.route('/getAll', methods=['GET'])
def getAll():
    return prioridadesReporteService.getAll()

@prioridadesReporte.route('/getid/<int:id>', methods=['GET'])
def getid(id):
    return prioridadesReporteService.getId(id)

@prioridadesReporte.route('/save', methods=['POST'])
def save():
    return prioridadesReporteService.save(request.get_json())

@prioridadesReporte.route('/update', methods=['PUT'])
def update():
    return prioridadesReporteService.update(request.get_json())

@prioridadesReporte.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return prioridadesReporteService.delete(id)
