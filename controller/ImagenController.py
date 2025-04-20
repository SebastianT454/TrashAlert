from flask import Blueprint, request
from service.ImagenService import ImagenService


# nombre variable: imagen


# Definir el Blueprint
imagen = Blueprint('imagen', __name__)
imagen_service = ImagenService()

@imagen.route('/classify', methods=['POST'])
def classify():
    return imagen_service.classify(
        image_bytes=request.files['imagen'].read(),
        mime_type=request.files['imagen'].mimetype
    )