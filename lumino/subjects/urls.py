from django.urls import path, register_converter

from . import converters, views

app_name = 'subjects'
register_converter(converters.SubjectConverter, 'subject')

urlpatterns = [
    path('', views.subject_list, name='subject-list'),
    path('<subject:subject>/', views.subject_detail, name='subject-detail'),
    path('enroll/', views.subject_enroll, name='subject-enroll'),
]
