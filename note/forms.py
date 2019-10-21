from django import forms

from .models import Notes


class NoteCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Notes
        fields = ('title', 'text', 'password',)


class NoteDetailForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Notes
        fields = ('password',)


class NoteEdithForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Notes
        fields = ('title', 'text', 'password',)
