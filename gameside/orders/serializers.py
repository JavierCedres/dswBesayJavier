from games.serializers import GameSerializer
from shared.serializers import BaseSerializer

from .models import Order


class OrderSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'status': instance.get_status_display(),
            'key': str(instance.key) if instance.status == Order.Status.PAID else None,
            'games': GameSerializer(instance.games.all(), request=self.request).serialize(),
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'price': instance.price,
        }
