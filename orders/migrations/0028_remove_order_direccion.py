# Generated by Django 3.0.4 on 2020-08-07 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_order_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='direccion',
        ),
    ]
