from django.shortcuts import render
from users.models import Profile


def subject_list(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        subjects = request.user.teaching.all()
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects))
    else:
        subjects = request.user.enrolled.all()
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects))


def subject_detail(request, subject):
    return render(request, 'subjects/subject/detail.html', dict(subject=subject))


def subject_enroll(request):
    return render(request, 'subjects/subject/enroll.html')
