from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, FormView

from .models import Notes
from category.models import Categories
from .forms import NoteCreateForm, NoteDetailForm


class NoteCreateView(FormView):
    def post(self, request, *args, **kwargs):
        category = Categories.objects.get(slug=kwargs['slug'])
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.password = make_password(form.cleaned_data['password'])
            print(note.password)
            note.category = category
            note.save()
            return redirect('note_detail', slug=note.slug)
        else:
            return render(request, 'note/new_note.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = NoteCreateForm()
        return render(request, 'note/new_note.html', {'form': form})


class NoteDetailView(FormView, DetailView):
    model = Notes
    form_class = NoteDetailForm
    template_name = 'note/note_enterpsw.html'

    def post(self, request, *args, **kwargs):
        note = Notes.objects.get(slug=kwargs['slug'])
        password = note.password
        title = note.title
        text = note.text

        form = NoteDetailForm(request.POST)
        if form.is_valid():
            passwordentered = form.cleaned_data.get("password")
            print(passwordentered)
            print(password)
            matchcheck = check_password(passwordentered, password)
            print(matchcheck)
            if matchcheck:
                return render(request, 'note/note_detail.html', {'title': title, 'text': text})
            else:
                return redirect('note_detail', slug=note.slug)
        else:
            return render(request, 'note/note_enterpsw.html', {'form': form})



