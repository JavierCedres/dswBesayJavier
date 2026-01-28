from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.decorators import require_http_methods
from users.decorators import auth_required

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
def order_detail(request, order_pk):
    try:
        order = Order.objects.get(pk=order_pk)
        print(order.games.all())
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    serializer = OrderSerializer(order, request=request)

    if order.user.pk != request.user.pk:
        return JsonResponse({'error': 'User is not the owner of requested order'}, status=403)

    return serializer.json_response()
