# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-17 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPJOGA', '0005_auto_20200916_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy_skill',
            name='reduc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minion_skill',
            name='reduc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='reduc',
            field=models.IntegerField(default=0),
        ),
    ]