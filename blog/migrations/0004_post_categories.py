# Generated by Django 3.0.4 on 2020-04-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoriasblog', '0001_initial'),
        ('blog', '0003_auto_20200430_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='categoriasblog.Category', verbose_name='Categorías'),
        ),
    ]
