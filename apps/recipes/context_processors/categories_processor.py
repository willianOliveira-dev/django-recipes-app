from django.http import HttpRequest

from core.services import services


def categories_processor(request: HttpRequest):
    categories = services.category.get_category_all()
    return {"categories": categories}
