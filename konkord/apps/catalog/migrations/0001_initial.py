# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 13:30
from __future__ import unicode_literals

import catalog.fields.thumbnail
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalogousProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', catalog.fields.thumbnail.ImageWithThumbnailsField(upload_to='catalog/products', verbose_name='Image')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('product_type', models.IntegerField(choices=[(0, 'Standard'), (1, 'Product with variants'), (2, 'Variant')], default=0, verbose_name='Type of product')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('sku', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sku')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='Full description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Price')),
                ('retail_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Retail price')),
                ('sale', models.BooleanField(default=False, verbose_name='Sale')),
                ('sale_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Sale price')),
                ('meta_title', models.TextField(blank=True, null=True, verbose_name='Meta title')),
                ('meta_h1', models.TextField(blank=True, null=True, verbose_name='Meta H1')),
                ('meta_keywords', models.TextField(blank=True, null=True, verbose_name='Meta keywords')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta description')),
                ('seo_text', models.TextField(blank=True, null=True, verbose_name='SEO text')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='catalog.Product', verbose_name='Parent')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPropertyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('slug_value', models.SlugField(max_length=255, verbose_name='Slug')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSorting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('order_by', models.CharField(max_length=255, verbose_name='Order by')),
                ('position', models.PositiveIntegerField(default=9999, verbose_name='Position')),
                ('css_class', models.CharField(blank=True, max_length=100, null=True, verbose_name='CSS class')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('show_buy_button', models.BooleanField(default=False, verbose_name='Show buy button')),
                ('is_visible', models.BooleanField(verbose_name='Is visible')),
                ('in_search', models.BooleanField(verbose_name='In search')),
                ('css_class', models.CharField(blank=True, max_length=100, null=True, verbose_name='CSS class')),
                ('position', models.PositiveIntegerField(default=9999, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='productpropertyvalue',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Property', verbose_name='Value'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductStatus'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.Product'),
        ),
        migrations.AddField(
            model_name='analogousproducts',
            name='analogous_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analogous', to='catalog.Product', verbose_name='Analogous products'),
        ),
        migrations.AddField(
            model_name='analogousproducts',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product'),
        ),
    ]
