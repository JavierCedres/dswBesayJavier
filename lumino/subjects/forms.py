from django import forms

from .models import Subject, Lesson, Enrollment


class AddEnrollSubjectsForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, student, *args, **kwargs):
        qs = Subject.objects.exclude(students=student)
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = qs
        

class DeleteEnrollSubjectsForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, student, *args, **kwargs):
        qs = Subject.objects.filter(students=student)
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = qs
        

class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']

    def save(self, subject, *args, **kwargs):
        lesson = super().save(commit=False)
        lesson.subject = subject
        lesson = super().save(*args, **kwargs)
        return lesson
    

class EditLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']
        

class EditMarkForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['mark']