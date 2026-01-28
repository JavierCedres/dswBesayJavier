import json
from http import HTTPStatus

from django.http import JsonResponse


def require_http_methods(*methods):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method not in methods:
                return JsonResponse(
                    {'error': 'Method not allowed'}, status=HTTPStatus.METHOD_NOT_ALLOWED
                )
            return func(request, *args, **kwargs)

        return wrapper

    return decorator


def validate_json_body(required_fields):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            try:
                payload = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON body'}, status=HTTPStatus.BAD_REQUEST)

            if any(field not in payload for field in required_fields):
                return JsonResponse(
                    {'error': 'Missing required fields'}, status=HTTPStatus.BAD_REQUEST
                )
            return func(request, *args, **kwargs)

        return wrapper

    return decorator
