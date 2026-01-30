import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import require_http_methods, validate_json_body
from users.decorators import auth_required

from .models import Game, Review
from .serializers import GameSerializer, ReviewSerializer


@csrf_exempt
@require_http_methods('GET')
def game_list(request):
    category_slug = request.GET.get('category')
    platform_slug = request.GET.get('platform')

    games = Game.objects.all()

    if category_slug:
        games = games.filter(category__slug=category_slug)

    if platform_slug:
        games = games.filter(platforms__slug=platform_slug)

    serializer = GameSerializer(games.distinct(), request=request)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
def game_detail(request, game_slug):
    try:
        game = Game.objects.get(slug=game_slug)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    serializer = GameSerializer(game, request=request)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
def review_list(request, game_slug):
    try:
        game = Game.objects.get(slug=game_slug)
        reviews = Review.objects.filter(game=game)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    serializer = ReviewSerializer(reviews, request=request)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
def review_detail(request, review_pk):
    try:
        review = Review.objects.get(pk=review_pk)
    except Review.DoesNotExist:
        return JsonResponse({'error': 'Review not found'}, status=404)
    serializer = ReviewSerializer(review, request=request)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('POST')
@validate_json_body(['rating', 'comment'])
@auth_required
def add_review(request, game_slug):
    payload = json.loads(request.body)

    try:
        game = Game.objects.get(slug=game_slug)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)

    if int(payload['rating']) < 1 or int(payload['rating']) > 5:
        return JsonResponse({'error': 'Rating is out of range'}, status=400)

    review = Review.objects.create(
        rating=payload['rating'], comment=payload['comment'], game=game, author=request.user
    )

    return JsonResponse({'id': review.pk})
