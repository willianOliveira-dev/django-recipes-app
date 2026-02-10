class ServiceFacade:
    """
    Centralizador de serviços para evitar múltiplas instâncias nas views.
    Utiliza o padrão Lazy Loading para performance.
    """

    def __init__(self) -> None:
        self._recipe = None
        self._category = None

    @property
    def recipe(self):
        if self._recipe is None:
            from apps.recipes.services.recipe.recipe_service import RecipeService

            self._recipe = RecipeService()

        return self._recipe

    @property
    def category(self):
        if self._category is None:
            from apps.recipes.services.category.category_service import CategoryService

            self._category = CategoryService()

        return self._category


services = ServiceFacade()
