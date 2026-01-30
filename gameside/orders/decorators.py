from functools import wraps

from django.http import JsonResponse

from .models import Order


def order_required(view):
    @wraps(view)
    def inner(request, order_pk, *args, **kwargs):
        try:
            order = Order.objects.get(pk=order_pk)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

        if order.user_id != request.user.pk:
            return JsonResponse({'error': 'User is not the owner of requested order'}, status=403)

        return view(request, order, *args, **kwargs)

    return inner
