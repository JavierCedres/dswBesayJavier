from django.conf import settings
from django.db import models


class Profile(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'STU', 'Student'
        TEACHER = 'TEA', 'Teacher'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profiles', on_delete=models.CASCADE
    )
    role = models.CharField(max_length=3, choices=Role, default=Role.STUDENT)
    avatar = models.ImageField(upload_to='media', default='media/noavatar.png', blank=True)
    bio = models.TextField(blank=True)
