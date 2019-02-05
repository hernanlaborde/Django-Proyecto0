from django.urls import path

from .views import (
    CategoriaListView, EventoListView, EventoDetailView, EventoCreateView,
    EventoUpdateView, EventoDeleteView
    )

app_name = 'eventos'
urlpatterns = [
    path('', EventoListView.as_view(), name='evento_list'),
    path('<int:pk>/', EventoDetailView.as_view(), name='evento_detail'),
    path('create/', EventoCreateView.as_view(), name='evento_create'),
    path('<int:pk>/update/', EventoUpdateView.as_view(), name='evento_update'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='evento_delete'),
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
]