# Generated by Django 4.2.7 on 2024-05-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookEaseApp', '0002_alter_bus_arrival_time_alter_bus_departure_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='arrival_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bus',
            name='departure_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.CharField(max_length=100),
        ),
    ]