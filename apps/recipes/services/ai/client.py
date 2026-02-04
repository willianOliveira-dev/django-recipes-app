import os

import httpx

from apps.recipes.services.ai.prompts import build_image_prompt, build_prompt


class HuggingFaceClient:
    def __init__(self) -> None:
        self.HF_API_KEY = os.getenv("HF_API_KEY")
        self.HF_TEXT_URL = os.getenv("HF_TEXT_URL")
        self.HF_IMAGE_URL = os.getenv("HF_TEXT_URL")

    def generate_recipe(self) -> str:
        try:
            with httpx.Client(timeout=60) as clientHttp:
                if not self.HF_API_KEY or not self.HF_TEXT_URL:
                    raise ValueError("HF_API_KEY ou HF_URL não configuradas.")
                headers = {"Authorization": f"Bearer {self.HF_API_KEY}"}

                payload = {
                    "inputs": build_prompt(),
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "return_full_text": False,
                    },
                }

                response = clientHttp.post(self.HF_TEXT_URL, headers=headers, json=payload)

            response.raise_for_status()

            data = response.json()

            print(data)

            text_output = data[0]["generated_text"]

            return str(text_output)

        except httpx.HTTPStatusError as _:
            raise ValueError("Erro ao gerar receita com IA.")

    def generate_recipe_image(self, title: str) -> bytes:
        try:
            with httpx.Client(timeout=60) as clientHttp:
                if not self.HF_API_KEY or not self.HF_IMAGE_URL:
                    raise ValueError("HF_API_KEY ou HF_URL não configuradas.")

                headers = {"Authorization": f"Bearer {self.HF_API_KEY}"}

                payload = {
                    "inputs": build_image_prompt(title),
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "return_full_text": False,
                    },
                }

                response = clientHttp.post(self.HF_IMAGE_URL, headers=headers, json=payload)

                response.raise_for_status()

                print(response.json())

                return response.content

        except httpx.HTTPStatusError as _:
            raise ValueError("Erro ao gerar imagem da receita com IA.")
