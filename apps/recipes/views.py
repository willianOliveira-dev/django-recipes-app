from uuid import UUID

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(req: HttpRequest) -> HttpResponse:
    return render(
        req,
        "recipes/pages/home.html",
    )


def login(req: HttpRequest) -> HttpResponse:
    return render(req, "recipes/pages/login.html")


def recipes(req: HttpRequest) -> HttpResponse:
    return render(
        req,
        "recipes/pages/recipes.html",
    )


def recipe(req: HttpRequest, id: UUID) -> HttpResponse:
    return render(req, "recipes/pages/search.html")
