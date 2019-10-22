from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from . models import Categories
from .forms import CategoriesCreateForm


class CategoriesListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=request.user.username)
        categories = Categories.objects.filter(user=user)
        context = {'categories': categories}
        return render(request, "category/home.html", context=context)


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=request.user.username)
        form = CategoriesCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = user
            note.save()
            return redirect('home')
        else:
            return render(request, 'category/new_category.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = CategoriesCreateForm()
        return render(request, 'category/new_category.html', {'form': form})


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Categories
    template_name = 'category/category_detail.html'
