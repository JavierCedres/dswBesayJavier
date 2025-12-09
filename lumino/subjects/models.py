from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='enrollments', on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        'subjects.subject', related_name='enrollments', on_delete=models.CASCADE
    )
    enrolled_at = models.DateField(auto_now_add=True)
    mark = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True
    )


class Lesson(models.Model):
    subject = models.ForeignKey(
        'subjects.subject', related_name='lessons', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=256, blank=True)


class Subject(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=128)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subjects', on_delete=models.PROTECT
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='enrollment', blank=True
    )
