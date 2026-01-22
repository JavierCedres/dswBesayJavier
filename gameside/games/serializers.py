from shared.serializers import BaseSerializer
from categories.serializers import CategorySerializer
from platforms.serializers import PlatformSerializer

class GameSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'slug': instance.slug,
            'description': instance.description,
            'cover': instance.cover,
            'price': instance.price,
            'stock': instance.stock,
            'released_at': instance.released_at.isoformat(),
            'pegi': instance.pegi,
            'category': CategorySerializer(instance.category).serialize(),
            'platforms': PlatformSerializer(instance.platforms.all()).serialize(),
        }
