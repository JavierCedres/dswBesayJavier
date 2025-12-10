from django.urls import path

from . import views

# No definimos nombre de aplicación porque queremos que las
# URLs de autenticación sean globales (sin espacio de nombres).
# app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
