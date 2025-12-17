from django.shortcuts import redirect, render

from users.models import Profile

from .forms import AddEnrollSubjectsForm


def subject_list(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        subjects = request.user.teaching.all()
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects))
    else:
        subjects = request.user.enrolled.all()
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects))


def subject_detail(request, subject):
    return render(request, 'subjects/subject/detail.html', dict(subject=subject))


def enroll_subjects(request):
    if request.method == 'POST':
        if (form := AddEnrollSubjectsForm(request.POST, request.user)).is_valid():
            redirect('subjects:subject-list')

    else:
        form = AddEnrollSubjectsForm(request.user)
    return render(request, 'subjects/subject/enroll.html', dict(form=form))
