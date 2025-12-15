from django.shortcuts import render


def subject_list(request):
    enrollments = request.user.subjects.all()
    return render(request, 'subjects/subject/list.html', dict(enrollments=enrollments))
