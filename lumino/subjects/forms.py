from django import forms

from .models import Subject


class EnrollSubjectsForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())

    def __init__(self, student, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.
