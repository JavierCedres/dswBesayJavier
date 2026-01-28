from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.decorators import require_http_methods
from users.decorators import auth_required

from .models import Order


@csrf_exempt
@require_http_methods('POST')
@auth_required
def add_order(request):
    order = Order.objects.create(user=request.user)

    return JsonResponse({'id': order.pk})
