# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Review', verbose_name='Родитель'),
        ),
    ]
