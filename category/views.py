from django.views.generic import ListView, CreateView, DetailView

from . models import Categories


class CategoriesListView(ListView):
    model = Categories
    template_name = 'category/home.html'


class CategoriesCreateView(CreateView):
    model = Categories
    template_name = 'category/new_category.html'
    fields = ('title',)


class CategoryDetailView(DetailView):
    queryset = Categories.objects.filter().order_by('-created_on')
    template_name = 'category/category_detail.html'