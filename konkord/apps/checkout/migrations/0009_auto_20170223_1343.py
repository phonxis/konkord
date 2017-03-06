# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 13:43
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0008_auto_20170215_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True, verbose_name='Voucher number')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('effective_from', models.FloatField(default=0.0, help_text='Minimal price', verbose_name='Effective from')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('type', models.PositiveSmallIntegerField(choices=[('percentage', 'Percentage'), ('absolute', 'Absolute')], verbose_name='Discount type')),
                ('value', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9, verbose_name='Value')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('used_amount', models.PositiveSmallIntegerField(default=0, verbose_name='Used amount')),
                ('last_used_date', models.DateTimeField(blank=True, null=True, verbose_name='Last used date')),
                ('limit', models.PositiveSmallIntegerField(blank=True, default=1, null=True, verbose_name='Limit')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'Voucher',
                'verbose_name_plural': 'Vouchers',
                'ordering': ('creation_date', 'number'),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='voucher_discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9, verbose_name='Voucher discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Voucher', verbose_name='Voucher'),
        ),
    ]
