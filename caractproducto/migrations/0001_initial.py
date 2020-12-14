# Generated by Django 3.0.4 on 2020-03-05 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='respuesta segun pregunta anterior', max_length=100, verbose_name='Descripcion')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcionCaracteristica', to='productos.Producto', verbose_name='Opcion')),
            ],
            options={
                'verbose_name': 'opcionCaracteristica',
                'verbose_name_plural': 'opcionCaracteristicas',
                'ordering': ['id'],
            },
        ),
    ]