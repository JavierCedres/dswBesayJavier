from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('completed/', views.completed_tasks, name='completed-tasks'),
    path('pending/', views.pending_tasks, name='pending-tasks'),
    path('<slug:task_slug>/toggle/', views.toggle_status_task, name='complete-task'),
    path('<slug:task_slug>/delete/', views.delete_task, name='delete-task'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit-task'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
]
