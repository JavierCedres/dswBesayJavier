from django import forms

from .models import Subject


class AddEnrollSubjectsForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, student, *args, **kwargs):
        qs = Subject.objects.exclude(students=student)
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = qs
