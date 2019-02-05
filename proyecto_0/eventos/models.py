from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    cat_nombre = models.CharField(max_length = 30)

    def __str__(self):
        return self.cat_nombre

class Evento(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_inicio = models.DateField('Fecha de Inicio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('eventos:evento_detail', kwargs={'pk':self.pk})
