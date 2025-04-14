import json

from model import EstadosReporte
from repository.postgres.EstadosReporteRepository import EstadosReporteRepository

"""
INSTRUCCIONES:
Cambiar todo lo que diga EstadosReporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga estadosReporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: EstadosReporte
# nombre variable: estadosReporte

class EstadosReporteService:

    def __init__(self):
        self.repository = EstadosReporteRepository()


    def save(self, estadosReporte):
        obj = EstadosReporte()
        for key, value in estadosReporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.save(obj)))


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, estadosReporte):
        obj = EstadosReporte()
        for key, value in estadosReporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        return json.dumps(vars(self.repository.getId(id)))

    def getAll(self):
        return [json.dumps(vars(objeto)) for objeto in self.repository.getAll()]