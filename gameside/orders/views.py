import json
import re
from datetime import date, datetime

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

    return JsonResponse({'status': order.get_status_display()}, status=200)


@csrf_exempt
@require_http_methods('POST')
@validate_json_body(['card-number', 'exp-date', 'cvc'])
@auth_required
@order_required
def pay_order(request, order):
    CARD_NUMBER_REGEXP = r'^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    EXP_DATE_REGEXP = r'^(0[1-9]|1[0-2])[/]\d{4}$'
    CVC_REGEXP = r'[0-9]{3}'

    payload = json.loads(request.body)

    if not order.status == Order.Status.CONFIRMED:
        return JsonResponse({'error': 'Orders can only be paid when confirmed'}, status=400)

    if not re.search(CARD_NUMBER_REGEXP, payload['card-number']):
        return JsonResponse({'error': 'Invalid card number'}, status=400)

    if not re.search(EXP_DATE_REGEXP, payload['exp-date']):
        return JsonResponse({'error': 'Invalid expiration date'}, status=400)

    if not re.search(CVC_REGEXP, payload['cvc']):
        return JsonResponse({'error': 'Invalid CVC'}, status=400)

    if date.today().replace(day=1) > datetime.strptime(payload['exp-date'], '%m/%Y').date():
        return JsonResponse({'error': 'Card expired'}, status=400)

    order.status = Order.Status.PAID
    order.save()

    return JsonResponse({'status': order.get_status_display(), 'key': order.key})
