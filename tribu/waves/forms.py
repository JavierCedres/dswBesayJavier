from django import forms

from .models import Wave


class AddWaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)

    def save(self, user, echo, *args, **kwargs):
        wave = super().save(commit=False)
        wave.user = user
        wave.echo = echo
        wave = super().save(*args, **kwargs)
        return wave


class EditWaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)
