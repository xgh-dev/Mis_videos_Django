# Generated by Django 5.1.3 on 2024-11-14 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuarioID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('usuarioNombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoNombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('videoRuta', models.CharField(max_length=500)),
                ('videoTamaño', models.FloatField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis_videos.usuario')),
            ],
        ),
    ]
