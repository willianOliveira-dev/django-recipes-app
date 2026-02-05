from datetime import timedelta

from django.db.models import Avg, Count, F, Q
from django.utils import timezone

from apps.recipes.models import Recipe


class RecipeRepository:
    """Modelo principal para operações no banco de dados da Receita"""

    def __init__(self):
        self.model = Recipe

    def _get_base_queryset(self, is_published: bool = True):
        """
        Retorna o QuerySet base com joins otimizados e agregações de avaliação.
        """
        return (
            self.model.objects.select_related("category", "author")
            .annotate(rating_avg=Avg("ratings__rating"), rating_count=Count("ratings"))
            .filter(is_published=is_published)
        )

    def get_filtered_recipes(
        self, category_slug: str | None = None, search_term: str | None = None
    ):
        """
        Realiza busca dinâmica filtrando por slug de categoria e/ou termo textual
        incidindo sobre título e descrição.
        """
        queryset = self._get_base_queryset()

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | Q(description__icontains=search_term)
            ).distinct()

        return queryset.order_by("-created_at")

    def get_weekly_highlights(self, limit: int = 6):
        """
        Recupera as receitas com maior engajamento de avaliações nos últimos 7 dias.
        """
        last_week = timezone.now() - timedelta(days=7)
        return (
            self._get_base_queryset()
            .filter(ratings__created_at__gte=last_week)
            .order_by("-rating_avg")[:limit]
        )

    def get_featured(self, limit: int = 6):
        """
        Obtém as receitas mais recentes publicadas na plataforma.
        """
        return self._get_base_queryset().order_by("-created_at")[:limit]

    def get_most_viewed(self, limit: int = 6):
        """
        Lista as receitas com maior volume de tráfego, ordenadas por visualizações e nota média.
        """
        return self._get_base_queryset().filter().order_by("-views_count", "-rating_avg")[:limit]

    def get_top_rated(self, limit: int = 6):
        """
        Filtra receitas com a melhor pontuação média, exigindo ao menos uma avaliação registrada.
        """
        return (
            self._get_base_queryset()
            .filter(rating_count__gt=0)
            .order_by("-rating_avg", "-rating_count")[:limit]
        )

    def get_recipe_detail_by_slug(self, slug: str):
        """
        Retorna a instância da receita com carregamento otimizado de seções,
        ingredientes e métodos de preparo.
        """
        return (
            self._get_base_queryset()
            .prefetch_related(
                "sections__section_ingredient__ingredient", "sections__preparations"
            )
            .filter(slug=slug)
            .first()
        )

    def get_latest_ratings(self, recipe_id: int, limit: int = 3):
        """
        Recupera o histórico recente de avaliações de uma receita específica.
        """
        recipe = self.model.objects.filter(id=recipe_id).first()
        return recipe.ratings.all().order_by("-created_at")[:limit] if recipe else []  # type: ignore

    def increment_view_count(self, recipe_id: int):
        """
        Incrementa a visualização em uma receita específica.
        """
        return self.model.objects.filter(id=recipe_id).update(
            views_count=F("views_count") + 1
        )
