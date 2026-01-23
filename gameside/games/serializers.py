from categories.serializers import CategorySerializer
from platforms.serializers import PlatformSerializer
from shared.serializers import BaseSerializer
from users.serializers import UserSerializer


class GameSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'slug': instance.slug,
            'description': instance.description,
            'cover': self.build_url(instance.cover.url),
            'price': instance.price,
            'stock': instance.stock,
            'released_at': instance.released_at.isoformat(),
            'pegi': instance.pegi,
            'category': CategorySerializer(instance.category).serialize(),
            'platforms': PlatformSerializer(instance.platforms.all()).serialize(),
        }


class ReviewSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'rating': instance.rating,
            'comment': instance.comment,
            'game': GameSerializer(instance.game).serialize(),
            'author': UserSerializer(instance.author).serialize(),
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
        }
