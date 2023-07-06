import openai
from pydantic import BaseModel

openai.organization = 'org-GUZBn3AmV27CWf64Yhl5lZOM'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'programacion'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programacion de nivel Universitario , entregaras lo que se solicite en formato de texto.
        E.G
        Programacion
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response

