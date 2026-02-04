from django.contrib import admin
from nested_admin import nested

from apps.recipes.models import (
    Category,
    Favorite,
    Ingredient,
    PreparationMethod,
    Recipe,
    RecipeRating,
    RecipeSection,
    RecipeSectionIngredient,
)


class IngredientInSectionInline(nested.NestedTabularInline):
    model = RecipeSectionIngredient
    extra = 0
    autocomplete_fields = ["ingredient"]
    classes = ["collapse"]


class PreparationStepInSectionInline(nested.NestedTabularInline):
    model = PreparationMethod
    extra = 0
    fields = ("position", "step")
    sortable_field_name = "position"


class RecipeSectionInline(nested.NestedStackedInline):
    model = RecipeSection
    extra = 0
    inlines = [IngredientInSectionInline, PreparationStepInSectionInline]
    sortable_field_name = "position"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(nested.NestedModelAdmin):
    list_display = ("title", "author", "category", "is_published")
    list_filter = ("category", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [RecipeSectionInline]
    fieldsets = (
        (
            "Informações Principais",
            {
                "fields": (
                    ("title", "slug"),
                    (("description", "difficulty_level")),
                    "category",
                    "author",
                )
            },
        ),
        ("Mídia", {"fields": ("cover",)}),
        (
            "Tempo e porções",
            {
                "fields": (
                    ("preparation_time", "preparation_time_unit"),
                    ("cooking_time", "cooking_time_unit"),
                    ("servings", "serving_unit"),
                )
            },
        ),
        ("Status", {"fields": ("is_published",)}),
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeRating)
class RecipeRatingAdmin(admin.ModelAdmin):
    pass
