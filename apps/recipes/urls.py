from django.urls import path

from apps.recipes import views

app_name= "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipes, name="recipes"),
    path("recipes/<uuid:id>", views.recipe, name="recipe"),
    path("login/",  views.login, name="login")
]
