import json
import base64

from model import Reporte
from repository.postgres.ReporteRepository import ReporteRepository
from service.ImagenService import ImagenService

"""
INSTRUCCIONES:
Cambiar todo lo que diga Reporte, por el nombre de la nueva clase con la primera en mayuscula. Verificar mayusculas
Cambiar todo lo que diga reporte, por el nombre de la nueva clase con todo en minuscula. Verificar minusculas
"""

# clase de modelo: Reporte
# nombre variable: reporte

imagen_service = ImagenService()

class ReporteService:

    def __init__(self):
        self.repository = ReporteRepository()


    def convertToJson(self, obj):
        obj['fecha_reporte'] = obj.get('fecha_reporte').isoformat()
        obj['imagen'] = base64.b64encode(obj.get('imagen')).decode('utf-8')

    def save(self, reporte):
        reporte['id_prioridad'] = json.loads( imagen_service.classify(image_bytes=reporte.get('imagen'),mime_type=reporte.pop('mime_type')) ).get('response')

        obj = Reporte()
        for key, value in reporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        saved_obj = vars(self.repository.save(obj))
        self.convertToJson(saved_obj)
        return json.dumps(saved_obj)


    def delete(self, id):
        return {"id eliminado": self.repository.delete(id)}

    def update(self, reporte):
        obj = Reporte()
        for key, value in reporte.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return json.dumps(vars(self.repository.update(obj)))

    def getId(self, id):
        obj = vars(self.repository.getId(id))
        self.convertToJson(obj)
        return json.dumps(obj)

    def getAll(self):
        data = []
        for objeto in self.repository.getAll():
            objeto_transformado = vars(objeto)
            self.convertToJson(objeto_transformado)
            data.append(json.dumps(objeto_transformado))
            
        parsed_data = [json.loads(item) for item in data]
        return json.dumps(parsed_data, indent=4)