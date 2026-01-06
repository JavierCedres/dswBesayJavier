from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.forms import modelformset_factory

from users.models import Profile
from .forms import AddEnrollSubjectsForm, DeleteEnrollSubjectsForm, AddLessonForm, EditLessonForm, EditMarkForm
from .models import Subject, Lesson, Enrollment


@login_required
def subject_list(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        subjects = request.user.teaching.all()
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects))
    else:
        subjects = request.user.enrolled.all()
        graded = all(enrollment.mark is not None for enrollment in request.user.enrollments.all())
        return render(request, 'subjects/subject/list.html', dict(subjects=subjects, graded=graded))


@login_required
def subject_detail(request, subject_code):
    if request.user.profile.role == Profile.Role.STUDENT:
        if not request.user.enrolled.filter(code=subject_code).exists():
            return HttpResponseForbidden("You are not enrolled in this subject.")
        subject = get_object_or_404(Subject, code=subject_code)
        enrollment = subject.enrollments.get(student=request.user)
        return render(request, 'subjects/subject/detail.html', dict(subject=subject, enrollment=enrollment))
    else:
        if not request.user.teaching.filter(code=subject_code).exists():
            return HttpResponseForbidden("You are not teaching this subject.")
        subject = get_object_or_404(Subject, code=subject_code)
        return render(request, 'subjects/subject/detail.html', dict(subject=subject))


@login_required
def lesson_detail(request, subject_code, lesson_pk):
    if (not request.user.teaching.filter(code=subject_code).exists()) and (not request.user.enrolled.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You don't belong to this subject")
        
    subject = get_object_or_404(Subject, code=subject_code)
    lesson = get_object_or_404(subject.lessons, id=lesson_pk)
    return render(request, 'subjects/lesson/detail.html', dict(lesson=lesson))


@login_required
def add_lesson(request, subject_code):    
    if (request.user.profile.role == Profile.Role.STUDENT) or (not request.user.teaching.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You are not a Teacher or maybe you are not teaching this subject.")
    
    if request.method == 'POST':
        if (form := AddLessonForm(request.POST)).is_valid():
            subject = get_object_or_404(Subject, code=subject_code)
            form.save(subject)
            messages.success(request, 'Lesson was successfully added.')
            return redirect('subjects:subject-detail', subject_code)
    else:
        form = AddLessonForm()
    return render(request, 'subjects/lesson/add.html', dict(form=form))


@login_required
def mark_list(request, subject_code):
    if (request.user.profile.role == Profile.Role.STUDENT) or (not request.user.teaching.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You are not a Teacher or maybe you are not teaching this subject.")

    subject = get_object_or_404(Subject, code=subject_code)
    enrollments =subject.enrollments.all()

    return render(request, 'subjects/mark/list.html', dict(subject=subject, enrollments=enrollments))


@login_required
def edit_marks(request, subject_code):
    if (request.user.profile.role == Profile.Role.STUDENT) or (not request.user.teaching.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You are not a Teacher or maybe you are not teaching this subject.")
    
    subject = get_object_or_404(Subject, code=subject_code)
    
    MarkFormSet = modelformset_factory(Enrollment, EditMarkForm, extra=0)
    queryset = subject.enrollments.all()
    if request.method == 'POST':
        if (formset := MarkFormSet(queryset=queryset, data=request.POST)).is_valid():
            formset.save()
            messages.success(request, 'Marks were successfully saved.')
            return render(
                request,
                'subjects/mark/edit.html',
                dict(subject=subject, formset=formset),
            )
    else:
        formset = MarkFormSet(queryset=queryset)
    return render(
        request,
        'subjects/mark/edit.html',
        dict(subject=subject, formset=formset),
    )
    
    
@login_required
def delete_lesson(request, subject_code, lesson_pk):
    if (request.user.profile.role == Profile.Role.STUDENT) or (not request.user.teaching.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You are not a Teacher or maybe you are not teaching this subject.")
    
    Lesson.objects.get(pk=lesson_pk).delete()
    messages.success(request, 'Lesson was successfully deleted.')
    return redirect('subjects:subject-detail', subject_code)


@login_required
def edit_lesson(request, subject_code, lesson_pk):
    if (request.user.profile.role == Profile.Role.STUDENT) or (not request.user.teaching.filter(code=subject_code).exists()):
        return HttpResponseForbidden("You are not a Teacher or maybe you are not teaching this subject.")
    
    lesson = Lesson.objects.get(pk=lesson_pk)
    
    if request.method == 'POST':
        if (form := EditLessonForm(request.POST, instance=lesson)).is_valid():
            form.save()
            messages.success(request, 'Changes were successfully saved.')
            return render(request, 'subjects/lesson/edit.html', dict(form=form))
    else:
        form = EditLessonForm(instance=lesson)
    return render(request, 'subjects/lesson/edit.html', dict(form=form))


@login_required
def enroll_subjects(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        return HttpResponseForbidden("Teachers cannot enroll in subjects.")
    
    if request.method == 'POST':
        if (form := AddEnrollSubjectsForm(request.user, request.POST)).is_valid():
            messages.success(request, 'Successfully enrolled in the chosen subjects.')
            subjects = form.cleaned_data['subjects']
            request.user.enrolled.add(*subjects)
            return redirect('subjects:subject-list')
    else:
        form = AddEnrollSubjectsForm(request.user)
    return render(request, 'subjects/subject/enroll.html', dict(form=form))


@login_required
def unenroll_subjects(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        return HttpResponseForbidden("Teachers cannot unenroll from subjects.")
    
    if request.method == 'POST':
        if (form := DeleteEnrollSubjectsForm(request.user, request.POST)).is_valid():
            messages.success(request, 'Successfully unenrolled from the chosen subjects.')
            subjects = form.cleaned_data['subjects']
            request.user.enrolled.remove(*subjects)
            return redirect('subjects:subject-list')
    else:
        form = DeleteEnrollSubjectsForm(request.user)
    return render(request, 'subjects/subject/unenroll.html', dict(form=form))


@login_required
def request_certificate(request):
    if request.user.profile.role == Profile.Role.TEACHER:
        return HttpResponseForbidden("Teachers cannot request certificates.")
    
    graded = all(enrollment.mark is not None for enrollment in request.user.enrollments.all())
    if not graded:
        return HttpResponseForbidden("You must have all subjects graded to request a certificate.")
    
    return redirect('subjects:subject-list')