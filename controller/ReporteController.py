from flask import Blueprint, request
from service import ReporteService

"""
INSTRUCCIONES:
Cambiar todo lo que diga Reporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga reporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Reporte
# nombre variable: reporte


# Definir el Blueprint
reporte = Blueprint('reporte', __name__)
reporteService = ReporteService()

@reporte.route('/getAll', methods=['GET'])
def getAll():
    return reporteService.getAll()

@reporte.route('/getid/<int:id>', methods=['GET'])
def getid(id):
    return reporteService.getId(id)

@reporte.route('/save', methods=['POST'])
def save():
    return reporteService.save(request.get_json())

@reporte.route('/update', methods=['PUT'])
def update():
    return reporteService.update(request.get_json())

@reporte.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return reporteService.delete(id)
