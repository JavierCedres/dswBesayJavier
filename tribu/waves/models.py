from django.conf import settings
from django.db import models


class Wave(models.Model):
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='waves', on_delete=models.CASCADE
    )
    echo = models.ForeignKey('echos.Echo', related_name='waves', on_delete=models.CASCADE)
