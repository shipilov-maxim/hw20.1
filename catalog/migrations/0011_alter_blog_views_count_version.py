# Generated by Django 5.0 on 2024-03-08 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='Номер версии')),
                ('version_title', models.CharField(max_length=100, verbose_name='Название версии')),
                ('is_actual_version', models.BooleanField(default=False, verbose_name='Признак актуальной версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
