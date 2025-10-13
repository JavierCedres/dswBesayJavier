from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', dict(tasks=tasks))


def add_task(request):
    if (form := AddTaskForm(request.POST or None)).is_valid():
        task = form.save(commit=False)
        task.slug = slugify(task.name)
        task.save()
        return redirect('tasks:task-list')
    return render(request, 'tasks/task/add.html', dict(form=form))


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/detail.html', dict(task=task))


def completed_tasks(request):
    return render(request, 'tasks/task/completed.html')


def pending_tasks(request):
    task_pending = Task.objects.filter(completed=False)
    return render(request, 'tasks/task/pending.html', dict(tasks=task_pending))


def toggle_status_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.completed = not task.completed
    task.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_task(request, task_slug):
    Task.objects.get(slug=task_slug).delete()
    return redirect('tasks:task-list')
