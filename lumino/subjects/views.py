from django.shortcuts import render

from .models import Subject


def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject/list.html', dict())
