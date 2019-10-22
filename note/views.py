from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Notes
from category.models import Categories
from .forms import NoteCreateForm, NoteDetailForm, NoteEdithForm
from .utils import *


class NoteCreateView(LoginRequiredMixin, FormView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=request.user.username)
        category = Categories.objects.get(slug=kwargs['slug'])
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.password = make_password(form.cleaned_data['password'])
            text = note.text
            note.text = encrypt(note.text, note.password)
            note.user = user
            note.category = category
            note.save()
            return render(request, 'note/note_detail.html', {'title': note.title, 'text': text, 'slug': note.slug})
        else:
            return render(request, 'note/new_note.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = NoteCreateForm()
        return render(request, 'note/new_note.html', {'form': form})


class NoteDetailView(LoginRequiredMixin, FormView, DetailView):
    form_class = NoteDetailForm
    template_name = 'note/note_enterpsw.html'
    model = Notes

    def post(self, request, *args, **kwargs):
        note = Notes.objects.get(slug=kwargs['slug'])
        password = note.password
        title = note.title
        text = decrypt(note.text, password)
        form = NoteDetailForm(request.POST)
        if form.is_valid():
            passwordentered = form.cleaned_data.get("password")
            check = check_password(passwordentered, password)
            if check:
                return render(request, 'note/note_detail.html', {'title': title, 'text': text, 'slug': note.slug})
            else:
                return redirect('note_detail', slug=note.slug)
        else:
            return render(request, 'note/note_enterpsw.html', {'title': title, 'text': text})


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NoteEdithForm
    template_name = 'note/note_edit.html'

    def get(self, request, **kwargs):
        self.object = Notes.objects.get(slug=kwargs['slug'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.initial['text'] = decrypt(self.object.text, self.object.password)
        form.initial['password'] = None
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        form.instance.text = encrypt(form.instance.text, form.instance.password)
        return super(NoteUpdateView, self).form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'note/note_delete.html'
    success_url = reverse_lazy('home')


