# Generated by Django 3.0.4 on 2020-03-18 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caractproducto', '0008_caracteristica_entero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristica',
            name='entero',
        ),
        migrations.AlterField(
            model_name='caracteristica',
            name='minimo',
            field=models.IntegerField(default=1, verbose_name='Pedido minimo'),
        ),
    ]
