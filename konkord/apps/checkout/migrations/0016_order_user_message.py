# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20170420_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_message',
            field=models.TextField(blank=True, null=True, verbose_name='User message'),
        ),
    ]
