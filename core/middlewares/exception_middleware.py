from typing import Callable

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from core.exceptions.http_exceptions import (
    BadRequestException,
    ConflictException,
    HttpException,
)
from core.exceptions.http_status import HttpStatus


class GlobalExceptionCatchingMiddleware:
    """
    Middleware global para capturar exceções da aplicação
    e renderizar páginas de erro usando templates.
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            response = self.get_response(request)
            return response

        except (BadRequestException, ConflictException) as exc:
            return JsonResponse(
                {"message": exc.message, "status_code": exc.status_code}
            )

        except HttpException as exc:
            return render(
                request,
                f"errors/{exc.status_code}.html",
                context={
                    "message": exc.message,
                    "status_code": exc.status_code,
                },
                status=exc.status_code,
            )
        except Exception:
            return render(
                request,
                "errors/500.html",
                context={
                    "message": "Erro interno no servidor",
                    "status_code": HttpStatus.INTERNAL_SERVER_ERROR,
                },
                status=HttpStatus.INTERNAL_SERVER_ERROR,
            )
