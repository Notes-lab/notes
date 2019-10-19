from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='home'),
    path('category/new/', views.CategoriesCreateView.as_view(), name='new_category'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='detail_category'),
    path('note/<slug:slug>/', include('note.urls')),
]
