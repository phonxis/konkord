# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('place', models.PositiveIntegerField(choices=[(1, 'Head top'), (5, 'Head bottom'), (10, 'Body top'), (15, 'Body bottom')], verbose_name='Place')),
                ('snippet', models.TextField(verbose_name='Snippet')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Snippet',
                'verbose_name_plural': 'Snippets',
            },
        ),
    ]
