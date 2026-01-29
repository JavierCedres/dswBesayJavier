from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from games.serializers import GameSerializer
from shared.decorators import require_http_methods
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
