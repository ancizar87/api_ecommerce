# Generated by Django 3.0.4 on 2020-03-16 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20200315_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='UMedida',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='promociones',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='valorpromo',
        ),
    ]
