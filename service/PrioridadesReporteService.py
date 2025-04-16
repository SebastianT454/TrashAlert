import json

from model import PrioridadesReporte
from repository.postgres.PrioridadesReporteRepository import PrioridadesReporteRepository

"""
INSTRUCCIONES:
Cambiar todo lo que diga PrioridadesReporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga prioridadesReporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: PrioridadesReporte
# nombre variable: prioridadesReporte

class PrioridadesReporteService:

    def __init__(self):
        self.repository = PrioridadesReporteRepository()


    def save(self, prioridadesReporte):
        obj = PrioridadesReporte()
        for key, value in prioridadesReporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.save(obj)))


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, prioridadesReporte):
        obj = PrioridadesReporte()
        for key, value in prioridadesReporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        return json.dumps(vars(self.repository.getId(id)))

    def getAll(self):
        data = [json.dumps(vars(objeto)) for objeto in self.repository.getAll()]
        parsed_data = [json.loads(item) for item in data]
        return json.dumps(parsed_data, indent=4)