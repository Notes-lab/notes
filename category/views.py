from django.views.generic import ListView

from . models import Categories


class CategoriesListView(ListView):
    model = Categories
    template_name = 'home.html'
