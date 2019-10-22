from django import forms

from .models import Categories


class CategoriesCreateForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('title',)
