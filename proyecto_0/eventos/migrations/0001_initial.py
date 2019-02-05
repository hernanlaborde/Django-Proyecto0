# Generated by Django 2.1.5 on 2019-01-30 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Categoria')),
            ],
        ),
    ]