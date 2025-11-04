from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class User(admin.ModelAdmin):
    list_display = ('id', 'user')
