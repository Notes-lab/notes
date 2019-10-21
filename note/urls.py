from django.urls import path, include

from . import views

urlpatterns = [
    path('new_note', views.NoteCreateView.as_view(), name='new_note'),
    path('', views.NoteDetailView.as_view(), name='note_detail'),
    path('edit', views.NoteUpdateView.as_view(), name='note_edit'),
    path('delete', views.NoteDeleteView.as_view(), name='note_delete'),
]
