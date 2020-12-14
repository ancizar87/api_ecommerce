# Generated by Django 3.0.4 on 2020-03-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='valorpromo',
            field=models.CharField(default=2, max_length=50, verbose_name='Precio Promocion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='Productos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=50, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='promociones',
            field=models.BooleanField(verbose_name='Promociones'),
        ),
    ]
