# Generated by Django 3.0.4 on 2020-04-19 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caractproducto', '0009_auto_20200317_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caractproducto.Caracteristica')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('precio_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('invoice_no', models.CharField(blank=True, default=orders.models.increment_invoice_number, max_length=500, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
