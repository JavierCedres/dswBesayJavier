from django.conf import settings
from django.db import models


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars', default='avatars/noavatar.png')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
