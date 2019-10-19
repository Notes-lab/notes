from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic import DetailView, FormView

from .models import Notes
from category.models import Categories
from .forms import NoteCreateForm


class NoteCreateView(FormView):
    def post(self, request, *args, **kwargs):
        category = Categories.objects.get(slug=kwargs['slug'])
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.password = make_password(form.cleaned_data['password'])
            note.category = category
            note.save()
            return redirect('note_detail', slug=note.slug)
        else:
            return render(request, 'note/new_note.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = NoteCreateForm()
        return render(request, 'note/new_note.html', {'form': form})


class NoteDetailView(DetailView):
    model = Notes
    template_name = 'note/note_detail.html'
    # model = Notes
    # template_name = 'note/new_note.html'
    # fields = ('title', 'text', 'password')
