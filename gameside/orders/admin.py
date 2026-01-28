from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdin(admin.ModelAdmin):
    list_display = ('user',)
