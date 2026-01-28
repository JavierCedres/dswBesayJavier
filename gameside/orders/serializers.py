from games.serializers import GameSerializer
from shared.serializers import BaseSerializer
from users.serializers import UserSerializer


class OrderSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            #'id': instance.pk,
            'key': instance.key,
            'user': UserSerializer(instance.user, request=self.request).serialize(),
            'games': GameSerializer(instance.games, request=self.request).serialize(),
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
        }
