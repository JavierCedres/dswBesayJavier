from django.conf import settings
from django.db import models


class Profile(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'S', 'Student'
        TEACHER = 'T', 'Teacher'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
    role = models.CharField(max_length=1, choices=Role, default=Role.STUDENT)
    avatar = models.ImageField(upload_to='avatars', default='avatars/noavatar.png', blank=True)
    bio = models.TextField(blank=True)
