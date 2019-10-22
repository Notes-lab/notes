from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        error_messages = {
            'username':
                {'unique': 'User with this name already exists.'},
            'email':
                {'unique': 'User with this email already exists'},
        }
