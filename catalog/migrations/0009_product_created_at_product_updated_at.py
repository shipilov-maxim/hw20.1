# Generated by Django 5.0 on 2024-02-13 11:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_product_created_at_remove_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата последнего изменения'),
            preserve_default=False,
        ),
    ]