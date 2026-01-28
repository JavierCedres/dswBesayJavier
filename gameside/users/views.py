import json

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import require_http_methods, validate_json_body


@csrf_exempt
@require_http_methods('POST')
@validate_json_body(['username', 'password'])
def auth(request):
    payload = json.loads(request.body)

    if user := authenticate(username=payload['username'], password=payload['password']):
        try:
            return JsonResponse({'token': user.token.key})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Token not found'}, status=404)
    return JsonResponse({'error': 'Invalid credentials'}, status=401)
