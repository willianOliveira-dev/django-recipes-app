from django.db.models import Avg, Count, Prefetch

from apps.recipes.models import Category, Recipe


class CategoryRepository:
    """Modelo principal para operaçõe no banco de dados da Categoria"""

    def __init__(self) -> None:
        self.model = Category
        self.recipe_model = Recipe

    def get_category_all(self):
        return self.model.objects.all()

    def get_filtered(
        self,
        slug: str | None = None,
        difficulty: str | None = None,
        sort: str | None = None,
    ):
        recipes_queryset = self.recipe_model.objects.annotate(
            rating_avg=Avg("ratings__rating"),
            rating_count=Count("ratings", distinct=True),
        )

        if difficulty:
            recipes_queryset = recipes_queryset.filter(difficulty_level=difficulty)

        if sort:
            order_by = {
                "asc": "created_at",
                "desc": "-created_at",
                "most_rated": "-rating_avg",
                "most_viewed": "-viewed_count",
            }
            recipes_queryset = recipes_queryset.order_by(order_by[sort])

        queryset = (
            (self.model.objects.filter(slug=slug) if slug else self.model.objects.all())
            .prefetch_related(Prefetch("recipes", queryset=recipes_queryset))
            .annotate(recipes_count=Count("recipes", distinct=True))
        )

        category = queryset.first()

        return {
            "category": category,
            "recipes": category.recipes.all() if category else [],  # type: ignore
        }
