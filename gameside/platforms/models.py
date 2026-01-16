from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=250, blank=True)
    logo = models.ImageField(
        upload_to='platforms/logos/', default='platforms/logos/default.png', blank=True
    )

    def __str__(self):
        return self.name
