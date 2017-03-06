# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 09:38
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_voucher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='voucher_discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=9, null=True, verbose_name='Voucher discount'),
        ),
    ]
