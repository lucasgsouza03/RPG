# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-15 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPJOGA', '0003_auto_20190721_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='char',
            name='dcrit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='char',
            name='dmin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
