import json

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.decorators import require_http_methods


@csrf_exempt
@require_http_methods('POST')
def auth(request):
    payload = json.loads(request.body)
    username = payload['username']
    password = payload['password']
    if user := authenticate(username=username, password=password):
        try:
            return JsonResponse({'token': user.token.key})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Token not found'}, status=404)
    return JsonResponse({'error': 'Invalid credentials'}, status=401)