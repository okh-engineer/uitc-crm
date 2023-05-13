# Generated by Django 4.2.1 on 2023-05-13 10:50

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=100, unique=True, verbose_name='Nomi'), unique=True)),
                ('address', models.CharField(max_length=250, verbose_name='Manzil')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Filiallar',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=100, unique=True, verbose_name='Nomi'), unique=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=8, default=100000, max_digits=10, null=True, verbose_name='Kurs narxi')),
                ('duration', models.PositiveIntegerField(default=1, verbose_name='Kurs davomiyligi')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1, verbose_name='Xona raqami')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=main_app.models.slugify_two_fields, verbose_name='slug')),
                ('capacity', models.PositiveIntegerField(default=8, verbose_name="Xona sig'imi")),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.branch', verbose_name='Filial')),
            ],
            options={
                'verbose_name': 'Xona',
                'verbose_name_plural': 'Xonalar',
                'ordering': ('-created_at',),
            },
        ),
    ]
