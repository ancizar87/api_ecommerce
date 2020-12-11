# Generated by Django 3.0.4 on 2020-05-05 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orientacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientacion', models.CharField(blank=True, max_length=50, verbose_name='Orientacion')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('subtitulo', models.CharField(max_length=50, verbose_name='Subtitulo')),
                ('link', models.CharField(max_length=50, verbose_name='Link')),
                ('imagenfondo', models.ImageField(upload_to=None, verbose_name='Imagenfondo')),
                ('imagenfrontal', models.ImageField(upload_to=None, verbose_name='Imagenfrontal')),
                ('orientacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banner.Orientacion', verbose_name='Orientacion')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['-id'],
            },
        ),
    ]