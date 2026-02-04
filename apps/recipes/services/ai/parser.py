import ast


def parse_recipe(text_output: str) -> dict:
    data = ast.literal_eval(text_output)

    if not isinstance(data, dict):
        raise ValueError("Resposta de IA inválida.")

    return data
