from django.contrib import admin

from .models import Echo


@admin.register(Echo)
class WaveAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content')
