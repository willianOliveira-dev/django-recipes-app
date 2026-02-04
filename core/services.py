class ServiceFacade:
    """
    Centralizador de serviços para evitar múltiplas instâncias nas views.
    Utiliza o padrão Lazy Loading para performance.
    """

    def __init__(self) -> None:
        self._recipe = None

    @property
    def recipe(self):
        if self._recipe is None:
            from apps.recipes.services.recipe.recipe_service import RecipeService

            self._recipe = RecipeService()

        return self._recipe

    ...


services = ServiceFacade()
