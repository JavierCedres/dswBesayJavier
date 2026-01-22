from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from .models import Game
from .serializers import GameSerializer


@csrf_exempt
@require_GET
def game_list(request):
    posts = Game.objects.all()
    serializer = GameSerializer(posts)
    return serializer.json_response()


@csrf_exempt
@require_GET
def game_detail(request, game_slug: str):
    try:
        game = Game.objects.get(slug=game_slug)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    serializer = GameSerializer(game)
    return serializer.json_response()
