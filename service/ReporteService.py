import json

from model import Reporte
from repository.postgres.ReporteRepository import ReporteRepository

"""
INSTRUCCIONES:
Cambiar todo lo que diga Reporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga reporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Reporte
# nombre variable: reporte

class ReporteService:

    def __init__(self):
        self.repository = ReporteRepository()


    def save(self, reporte):
        obj = Reporte()
        for key, value in reporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.save(obj)))


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, reporte):
        obj = Reporte()
        for key, value in reporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        return json.dumps(vars(self.repository.getId(id)))

    def getAll(self):
        return [json.dumps(vars(objeto)) for objeto in self.repository.getAll()]