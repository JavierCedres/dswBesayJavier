from django.urls import path, register_converter
from django.shortcuts import redirect

from . import views, converters

app_name = "users"
register_converter(converters.ProfileConverter, "profile")

urlpatterns = [
    path('', views.user_list, name="user-list"),
    path('<profile:profile>/', views.user_detail, name='user-detail'),
    path('<profile:profile>/echos/', views.user_echos, name='user-echos'),
    path('<profile:profile>/edit/', views.user_edit, name='user-edit'),
    path('@me/', views.my_user_detail, name='my-user-detail'),
]