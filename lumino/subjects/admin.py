from django.contrib import admin

from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'teacher', 'students')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'content')


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'enrolled_at', 'mark')
