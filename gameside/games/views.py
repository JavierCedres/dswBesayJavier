from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import require_http_methods


@csrf_exempt
@require_http_methods
def game_list(request):
    return JsonResponse({'success': 'Hola'}, status=200)
