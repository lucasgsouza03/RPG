# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='char',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('identificador', models.CharField(blank=True, max_length=150)),
                ('forca', models.IntegerField()),
                ('habilidade', models.IntegerField()),
                ('agilidade', models.IntegerField()),
                ('dex', models.IntegerField()),
                ('inteligencia', models.IntegerField()),
                ('forc_vont', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('estamina', models.IntegerField()),
                ('base_hp', models.IntegerField()),
                ('base_estamina', models.IntegerField()),
                ('dmin', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'perfil',
            },
        ),
        migrations.CreateModel(
            name='debuf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('duracao', models.IntegerField()),
            ],
            options={
                'db_table': 'debuf',
            },
        ),
        migrations.CreateModel(
            name='enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('hp', models.IntegerField()),
                ('hp_base', models.IntegerField(blank=True)),
                ('esquiva', models.CharField(max_length=5)),
                ('block', models.CharField(max_length=5)),
                ('dmin', models.IntegerField()),
            ],
            options={
                'db_table': 'enemy',
            },
        ),
        migrations.CreateModel(
            name='enemy_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cd', models.IntegerField()),
                ('cd_corrent', models.IntegerField(default=0)),
                ('duracao', models.IntegerField()),
                ('duracao_corrent', models.IntegerField(default=0)),
                ('reduc', models.IntegerField()),
                ('dano', models.IntegerField(blank=True)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('enemy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.enemy')),
            ],
            options={
                'db_table': 'enemy_skill',
            },
        ),
        migrations.CreateModel(
            name='enemy_stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('hp', models.IntegerField()),
                ('hp_base', models.IntegerField(blank=True)),
                ('esquiva', models.CharField(max_length=5)),
                ('block', models.CharField(max_length=5)),
                ('dmin', models.IntegerField()),
                ('dresult', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'enemy_stage',
            },
        ),
        migrations.CreateModel(
            name='invent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('nome', models.CharField(max_length=150)),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.char')),
            ],
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('mensagem', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'log',
            },
        ),
        migrations.CreateModel(
            name='minion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('hp', models.IntegerField()),
                ('hp_base', models.IntegerField(blank=True)),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.char')),
            ],
            options={
                'db_table': 'minion',
            },
        ),
        migrations.CreateModel(
            name='minion_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('identificador', models.CharField(blank=True, max_length=10)),
                ('cd', models.IntegerField()),
                ('cd_corrent', models.IntegerField(default=0)),
                ('duracao', models.IntegerField()),
                ('duracao_corrent', models.IntegerField(default=0)),
                ('reduc', models.IntegerField()),
                ('dano', models.IntegerField(blank=True)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('max_use', models.IntegerField(default=0)),
                ('max_use_corrent', models.IntegerField(default=0)),
                ('fist_turn', models.IntegerField(default=0)),
                ('minion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.minion')),
            ],
            options={
                'db_table': 'minion_skill',
            },
        ),
        migrations.CreateModel(
            name='minion_stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('hp', models.IntegerField()),
                ('hp_base', models.IntegerField(blank=True)),
                ('dresult', models.IntegerField(default=0)),
                ('char', models.IntegerField(default=0)),
                ('minion_id', models.IntegerField(default=0)),
                ('skill_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'minion_stage',
            },
        ),
        migrations.CreateModel(
            name='rodada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'rodada',
            },
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('identificador', models.CharField(max_length=10)),
                ('cd', models.IntegerField()),
                ('cd_corrent', models.IntegerField(default=0)),
                ('duracao', models.IntegerField()),
                ('duracao_corrent', models.IntegerField(default=0)),
                ('max_use', models.IntegerField()),
                ('max_use_corrent', models.IntegerField(default=0)),
                ('fist_turn', models.IntegerField(default=0)),
                ('reduc', models.IntegerField()),
                ('dano', models.IntegerField(blank=True)),
                ('bonus_dano', models.IntegerField(blank=True, null=True)),
                ('bonus_cost', models.IntegerField(blank=True, null=True)),
                ('estamina', models.IntegerField(blank=True)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.char')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.AddField(
            model_name='minion',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='RPJOGA.skill'),
        ),
    ]
