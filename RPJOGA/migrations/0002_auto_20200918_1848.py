# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-18 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPJOGA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='item_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='item_cost_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]