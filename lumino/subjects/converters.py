from django.shortcuts import get_object_or_404

from .models import Subject


class SubjectConverter:
    regex = r'[\w-]+'

    def to_python(self, code: str) -> Subject:
        return get_object_or_404(Subject, code=code)

    def to_url(self, subject: Subject) -> str:
        return subject
