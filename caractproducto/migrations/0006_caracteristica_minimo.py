# Generated by Django 3.0.4 on 2020-03-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caractproducto', '0005_auto_20200315_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristica',
            name='minimo',
            field=models.IntegerField(default=2, verbose_name='U. minima'),
            preserve_default=False,
        ),
    ]
