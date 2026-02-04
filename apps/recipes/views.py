from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from core.services import services


def home_view(req: HttpRequest) -> HttpResponse:
    """Exibe as prateleiras de receitas (Destaques, Semanal, Populares)."""

    data = services.recipe.get_home_data()

    return render(req, "recipes/pages/home.html", context=data)


def login(req: HttpRequest) -> HttpResponse:
    return render(req, "recipes/pages/login.html")


def recipe_search_view(req: HttpRequest) -> HttpResponse:
    """Filtra receitas por termo de busca e/ou categoria."""

    search_term = req.GET.get("q", "").strip()
    category_slug = req.GET.get("category", None)

    recipes = services.recipe.search_catalog(
        category_slug=category_slug, search_term=search_term
    )
    return render(
        req,
        "recipes/pages/recipes.html",
        context={
            "recipes": recipes,
            "search_term": search_term,
        },
    )


def recipe_detail_view(req: HttpRequest, slug: str) -> HttpResponse:
    recipe = services.recipe.get_recipe_detail(request=req, slug=slug)

    if not recipe:
        raise Http404("Receita não encontrada.")

    return render(req, "recipes/pages/recipe-detail.html", context={"recipe": recipe})
