from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def healingmentor_exception_handler(exc, context):
    """
    Customized exception handler for veronica

    Handler returns response with `error` and `detail`.

    """

    response = exception_handler(exc, context)
    print("ARR")

    if response is not None:
        response = Response(
            {
                "error": exc.get_codes(),
                "detail": exc.detail,
            },
            status=response.status_code,
        )

    return response


def bad_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """

    data = {
        "error": "bad_request",
        "detail": "Request format is incorrect.",
    }

    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


def page_not_found(request, exception, *args, **kwargs):
    """
    Generic 404 error handler.
    """

    data = {
        "error": "page_not_found",
        "detail": "The requested resource was not found on this server.",
    }

    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """

    data = {
        "error": "server_error",
        "detail": "There was an error while processing your request.",
    }

    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
