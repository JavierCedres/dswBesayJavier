from django.urls import path, register_converter

from . import converters, views

app_name = 'waves'
register_converter(converters.WaveConverter, 'wave')

urlpatterns = [
    path('<wave:wave>/delete/', views.delete_wave, name='delete-wave'),
    path('<wave:wave>/edit/', views.edit_wave, name='edit-wave'),
]
