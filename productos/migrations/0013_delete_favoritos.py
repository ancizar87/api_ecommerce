# Generated by Django 3.1.3 on 2020-12-11 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_favoritos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favoritos',
        ),
    ]
