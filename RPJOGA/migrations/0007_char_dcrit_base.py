# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-27 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPJOGA', '0006_skill_dcrit_mid'),
    ]

    operations = [
        migrations.AddField(
            model_name='char',
            name='dcrit_base',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
