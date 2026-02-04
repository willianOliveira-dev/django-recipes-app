from django.urls import path

from apps.recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("recipes/", views.recipe_search_view, name="recipes"),
    path("recipes/<slug:slug>", views.recipe_detail_view, name="recipe"),
    path("login/", views.login, name="login"),
]
