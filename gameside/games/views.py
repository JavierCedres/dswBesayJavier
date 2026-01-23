from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Game, Review
from .serializers import GameSerializer, ReviewSerializer


@csrf_exempt
@require_http_methods('GET')
def game_list(request):
    category_slug = request.GET.get('category', None)
    platform_slug = request.GET.get('platform', None)

    if category_slug and platform_slug:
        games = Game.objects.filter(category__slug=category_slug, platforms__slug=platform_slug)
    elif category_slug:
        games = Game.objects.filter(category__slug=category_slug)
    elif platform_slug:
        games = Game.objects.filter(platforms__slug=platform_slug)
    else:
        games = Game.objects.all()

    serializer = GameSerializer(games)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
def game_detail(request, game_slug: str):
    try:
        game = Game.objects.get(slug=game_slug)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    serializer = GameSerializer(game)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
def review_list(request, game_slug):
    try:
        game = Game.objects.get(slug=game_slug)
        reviews = Review.objects.get()
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    serializer = ReviewSerializer()
