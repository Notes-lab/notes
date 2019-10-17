from django.urls import path

from . import views

urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='home'),
    path('post/new/', views.CategoriesCreateView.as_view(), name='post_new'),
]
