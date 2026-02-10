from django.http import HttpRequest

from apps.recipes.repositories.recipe.recipe_repository import RecipeRepository


class RecipeService:
    def __init__(self) -> None:
        self.recipe_repo = RecipeRepository()

    def get_home_data(self):
        """
        Orquestra o conjunto de dados para a página inicial, incluindo destaques,
        populares e tendências semanais.
        """
        featured = self.recipe_repo.get_featured(6)
        weekly_highlights = self.recipe_repo.get_weekly_highlights(6)
        most_viewed = self.recipe_repo.get_most_viewed(9)
        top_rated = self.recipe_repo.get_top_rated(6)

        return {
            "weekly_highlights": weekly_highlights if weekly_highlights else top_rated,
            "featured": featured,
            "most_viewed": most_viewed,
        }

    def get_recipe_detail(self, request: HttpRequest, slug: str):
        """
        Retorna os detalhes da receita e gerencia o incremento de visualizações
        baseado na sessão do usuário ( logado ou anônimo ) para evitar duplicidade.
        """

        recipe = self.recipe_repo.get_recipe_detail_by_slug(slug)

        if recipe:
            session_key = f"viewed_recipe_{recipe.pk}"
            if not request.session.get(session_key):
                self.recipe_repo.increment_view_count(recipe_id=recipe.pk)
                request.session[session_key] = True

        return recipe

    def get_recipe_catalog(
        self, category_slug: str | None = None, search_term: str | None = None
    ):
        """
        Interface de busca para o catálogo de receitas com suporte a filtros combinados.
        """

        return self.recipe_repo.get_filtered_recipes(
            category_slug=category_slug, search_term=search_term
        )
