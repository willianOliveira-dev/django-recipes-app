from enum import Enum

from apps.recipes.repositories.category.category_repository import CategoryRepository
from core.exceptions.http_exceptions import BadRequestException


class SortOption(Enum):
    ASC = "asc"
    DESC = "desc"
    MOST_RATED = "most_rated"
    MOST_VIEWED = "most_viewed"


class DifficultyOption(Enum):
    EASY = "facil"
    AVERAGE = "medio"
    DIFFICULT = "dificil"
    EXPERT = "expert"


class CategoryService:
    def __init__(self) -> None:
        self.category_repo = CategoryRepository()

    def get_category_all(self):
        return self.category_repo.get_category_all()

    def get_recipes_by_category(
        self,
        slug: str | None = None,
        difficulty: str | None = None,
        sort: str | None = None,
    ):
        """
        Interface de busca para o catálogo de categorias + receitas com suporte a filtros combinados.
        """

        if sort:
            if sort not in SortOption._value2member_map_:
                raise BadRequestException(
                    "Parâmetro inválido. Use apenas: asc, desc, most_rated e most_viewed"
                )

        if difficulty:
            if difficulty not in DifficultyOption._value2member_map_:
                raise BadRequestException(
                    "Parâmetro inválido. Use apenas: facil, medio, dificil e expert"
                )

        data = self.category_repo.get_filtered(slug, difficulty=difficulty, sort=sort)

        return data
