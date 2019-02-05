from django.shortcuts import render

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Categoria, Evento

from .forms import EventoModelForm

from django.urls import reverse_lazy

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoModelForm
    #success_url = '/'  alternativa el reverse del modelo

class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoModelForm
    # success_url = '/'  alternativa el reverse del modelo


class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    queryset = Evento.objects.all() # <app_name>/<model_name>_list.html


class EventoDetailView(LoginRequiredMixin, DetailView):
    model = Evento
    #queryset = Evento.objects.all() # <app_name>/<model_name>_list.html


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:evento_list')
    #queryset = Evento.objects.all() # <app_name>/<model_name>_list.html


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    queryset = Categoria.objects.all() # <app_name>/<model_name>_list.html
