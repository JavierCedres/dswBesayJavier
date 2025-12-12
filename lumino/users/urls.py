from django.urls import path, register_converter

from . import converters, views

app_name = 'users'
register_converter(converters.ProfileConverter, 'profile')

urlpatterns = [
    path('<profile:profile>/', views.user_detail, name='user-detail'),
    path('<profile:profile>/edit/', views.leave, name='leave'),
    path('@me/', views.my_user_detail, name='my-user-detail'),
]
