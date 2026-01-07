from django.urls import path, register_converter

from . import converters, views

app_name = 'users'
register_converter(converters.ProfileConverter, 'profile')

urlpatterns = [
    path('users/@me/', views.my_user_detail, name='my-user-detail'),
    path('user/leave/', views.leave, name='leave'),
    path('user/edit/', views.edit_profile, name='edit-profile'),
    path('users/<str:username>/', views.user_detail, name='user-detail'),
]
