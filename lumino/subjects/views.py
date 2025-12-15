from django.shortcuts import render

from users.models import Profile


def subject_list(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        enrollments = request.user.teaching.all()
        return render(request, 'subjects/subject/list.html', dict(enrollments=enrollments))
    else:
        enrollments = request.user.enrolled.all()
        return render(request, 'subjects/subject/list.html', dict(enrollments=enrollments))
