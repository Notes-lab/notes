from django.views.generic import ListView, CreateView

from . models import Categories


class CategoriesListView(ListView):
    model = Categories
    template_name = 'category/home.html'


class CategoriesCreateView(CreateView):
    model = Categories
    template_name = 'category/new_category.html'
    fields = 'title'
