# Generated by Django 4.1.3 on 2022-11-18 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20221117_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='company',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traders', to='companies.company', verbose_name='Поставщик'),
        ),
    ]
