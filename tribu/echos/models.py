from django.conf import settings
from django.db import models
from django.urls import reverse


class Echo(models.Model):
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='echos', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('echos:echo-detail', args=[self.pk])

    def __str__(self):
        return str(self.pk)
