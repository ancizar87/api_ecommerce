# Generated by Django 3.0.4 on 2020-05-05 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caractproducto', '0011_auto_20200503_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caracteristica',
            old_name='cantidad',
            new_name='disponibles',
        ),
    ]
