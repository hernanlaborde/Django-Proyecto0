from django import forms
from .models import Evento


class EventoModelForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"Ingrese el nombre",
            }))
    fecha_inicio = forms.DateField(widget=forms.TextInput(
        attrs={
            'type':'date'
            }))

    class Meta:
        model = Evento
        fields = [
            'nombre', 'fecha_inicio', 'categoria'
        ]