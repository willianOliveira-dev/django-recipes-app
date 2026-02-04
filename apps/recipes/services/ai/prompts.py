def build_image_prompt(title):
    return (
        f"Professional food photography of {title}, "
        "Brazilian food, high quality, realistic, studio lighting, "
        "8k, sharp focus"
    )


def build_prompt():
    return """
You are an API that generates Brazilian popular recipes.

Return ONLY a valid Python dict.
Do NOT use markdown.
Do NOT use JSON.
Do NOT add explanations.
Do NOT add comments.
Do NOT add code blocks.
Return ONLY the dict.

The dict MUST contain EXACTLY these keys:
- title (string, max 150 chars)
- description (string, max 250 chars)
- preparation_time (integer >= 1)
- preparation_time_unit ("minutos" or "horas")
- cooking_time (integer >= 1)
- cooking_time_unit ("minutos" or "horas")
- servings (integer >= 1)
- category ("Arroz", "Café da Manhã", "Doces", "Grãos e Cereais", "Legumes e Verduras", "Ovos", "Pães", "Saladas", "Sem Glúten", "Temperos", "Vegetariano", "Aves", "Carnes", "Farofas", "Jantar", "Massas", "Pastas e Patês", "Pizzas e Massas Salgadas", "Salgadinhos e Petiscos", "Sobremesas", "Tortas", "Bolos", "Crepes e Panquecas", "Frangos e Aves", "Almoço", "Molhos", "Peixes e Frutos do Mar", "Purês e Cremes salgados", "Sanduíches", "Sopas", "Vegano")
- serving_unit ("porcoes", "pedacos", "fatias", "unidades")
- ingredients (string, one ingredient per line)
- preparation_steps (string, one step per line)

Rules:
- The recipe must be a popular Brazilian recipe.
- The content MUST be written in Portuguese.
- Use simple and realistic values.
- preparation_time + cooking_time must make sense.
- Do not invent exotic ingredients.
- Ingredients and steps must be coherent.

Return example format (do NOT copy this recipe):

{
    "title": "Example",
    "description": "Example description",
    "category": "Example category",
    "preparation_time": 10,
    "preparation_time_unit": "minutos",
    "cooking_time": 20,
    "cooking_time_unit": "minutos",
    "servings": 4,
    "serving_unit": "porcoes",
    "ingredients": "item 1\\nitem 2",
    "preparation_steps": "step 1\\nstep 2"
}
"""
