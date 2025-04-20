import json
from google import genai
from SecretConfig import GEMINI_API_KEY, GEMINI_PROMPT, ALLOWED_MIME_TYPES

class ImagenService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.prompt = GEMINI_PROMPT
        self.allowed_mime_types = ALLOWED_MIME_TYPES


    def validateImg(self, image_bytes, mime_type):
        if mime_type not in self.allowed_mime_types:
            raise ValueError(f"Tipo mime no permitido: {mime_type}, Tipos permitidos: {self.allowed_mime_types}")
 
    def classifyImg(self, image_bytes, mime_type):
        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=[
                genai.types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type,
                ),
                self.prompt
                ]
            )
            return {'response': response.text}
        except Exception as e:
            raise ValueError(f"El siguiente error ha ocurrido con el LLM: {e}")

    def classify(self, image_bytes, mime_type):
        try:
            self.validateImg(image_bytes, mime_type)

            response = self.classifyImg(image_bytes, mime_type)
            return json.dumps(response)
        
        except Exception as e:

            print(f"Un error ha ocurrido: {e}")
            return json.dumps({'invalid_image_request': str(e)})