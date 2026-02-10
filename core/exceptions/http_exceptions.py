from core.exceptions.http_status import HttpStatus

class HttpException(Exception):
    """Exceção base para erros HTTP com status code."""

    def __init__(self, message: str, status_code: HttpStatus) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class BadRequestException(HttpException):
    """Erro 400: requisição inválida."""

    def __init__(self, message: str = "Bad Request") -> None:
        super().__init__(message, HttpStatus.BAD_REQUEST)


class UnauthorizedException(HttpException):
    """Erro 401: autenticação necessária ou inválida."""

    def __init__(self, message: str = "Unauthorized") -> None:
        super().__init__(message, HttpStatus.UNAUTHORIZED)


class ForbiddenException(HttpException):
    """Erro 403: acesso negado ao recurso."""

    def __init__(self, message: str = "Forbidden") -> None:
        super().__init__(message, HttpStatus.FORBIDDEN)


class NotFoundException(HttpException):
    """Erro 404: recurso não encontrado."""

    def __init__(self, message: str = "Not Found") -> None:
        super().__init__(message, HttpStatus.NOT_FOUND)


class ConflictException(HttpException):
    """Erro 409: conflito de estado ou duplicidade."""

    def __init__(self, message: str = "Conflict") -> None:
        super().__init__(message, HttpStatus.CONFLICT)


class InternalServerErrorException(HttpException):
    """Erro 500: falha inesperada no servidor."""

    def __init__(self, message: str = "Internal Server Error") -> None:
        super().__init__(message, HttpStatus.INTERNAL_SERVER_ERROR)
