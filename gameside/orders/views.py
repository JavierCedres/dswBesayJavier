import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from games.models import Game
from games.serializers import GameSerializer
from shared.decorators import require_http_methods, validate_json_body
from users.decorators import auth_required

from .decorators import order_required
from .models import Order
from .serializers import OrderSerializer


@csrf_exempt
@require_http_methods('POST')
@auth_required
def add_order(request):
    order = Order.objects.create(user=request.user)

    return JsonResponse({'id': order.pk})


@csrf_exempt
@require_http_methods('GET')
@auth_required
@order_required
def order_detail(request, order):
    serializer = OrderSerializer(order, request=request)
    return serializer.json_response()


@csrf_exempt
@require_http_methods('GET')
@auth_required
@order_required
def order_game_list(request, order):
    return JsonResponse(GameSerializer(order.games.all(), request=request).serialize(), safe=False)


@csrf_exempt
@require_http_methods('POST')
@validate_json_body(['game-slug'])
@auth_required
@order_required
def add_game_to_order(request, order):
    payload = json.loads(request.body)
    try:
        game = Game.objects.get(slug=payload['game-slug'])
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)
    if game.stock == 0:
        return JsonResponse({'error': 'Game out of stock'}, status=400)
    game.stock -= 1
    order.games.add(game)
    return JsonResponse({'num-games-in-order': order.games.count()})


@csrf_exempt
@require_http_methods('POST')
@validate_json_body(['status'])
@auth_required
@order_required
def change_order_status(request, order):
    payload = json.loads(request.body)

    if payload['status'] == Order.Status.INITIATED or payload['status'] == Order.Status.PAID:
        return JsonResponse({'error': 'Invalid status'}, status=400)

    if not order.status == Order.Status.INITIATED:
        return JsonResponse(
            {'error': 'Orders can only be confirmed/cancelled when initiated'}, status=400
        )

    if payload['status'] == Order.Status.CANCELLED:
        for game in order.games.all():
            game.stock += 1

    order.status = payload['status']
    order.save()

    for status in Order.Status.choices:
        if order.status == status[0]:
            status_name = status[1]

    return JsonResponse({'status': status_name}, status=200)
