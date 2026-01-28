import json

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.decorators import require_http_methods


@csrf_exempt
@require_http_methods('POST')
def auth(request):
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    username = payload['username']
    password = payload['password']
    if not username or not password:
        return JsonResponse({'error': 'Missing required fields'}, status=400)
    if user := authenticate(username=username, password=password):
        try:
            return JsonResponse({'token': user.token.key})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Token not found'}, status=404)
    return JsonResponse({'error': 'Invalid credentials'}, status=401)
