from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.RedirectView.as_view(), name='index'),
    path('register/', views.register, name='register'),
]
