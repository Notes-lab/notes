from django import forms

from .models import Notes


class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('title', 'text', 'password',)
