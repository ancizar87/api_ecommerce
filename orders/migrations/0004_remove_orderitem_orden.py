# Generated by Django 3.0.4 on 2020-04-20 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='orden',
        ),
    ]
