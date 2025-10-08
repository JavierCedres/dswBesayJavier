from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=256, unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
