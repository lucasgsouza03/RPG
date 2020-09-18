from os import truncate
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class char(models.Model):
    nome = models.CharField(max_length=150)
    identificador = models.CharField(max_length=150, blank=True)
    forca = models.IntegerField()
    habilidade = models.IntegerField()
    agilidade = models.IntegerField()
    dex = models.IntegerField()
    inteligencia = models.IntegerField()
    forc_vont = models.IntegerField()
    hp = models.IntegerField() 
    estamina = models.IntegerField()
    base_hp =  models.IntegerField() 
    base_estamina = models.IntegerField()
    dmin = models.IntegerField(blank=True, null=True)
    dcrit = models.IntegerField(blank=True, null=True)
    reduc = models.IntegerField(default=0)

    class Meta:
        db_table = "perfil"
    def __str__(self):
        return self.nome

class log(models.Model):
    tipo = models.CharField(max_length=50)
    mensagem = models.CharField(max_length=500)

    class Meta:
        db_table = "log"
    def __str__(self):
        return self.tipo

class invent(models.Model):
    qtd = models.IntegerField()
    limit_qtd = models.IntegerField(default=0)
    nome = models.CharField(max_length=150)
    char = models.ForeignKey('char',
    on_delete=models.DO_NOTHING,)

class enemy(models.Model):
    nome = models.CharField(max_length=150)
    hp = models.IntegerField()
    hp_base = models.IntegerField(blank=True)
    esquiva = models.CharField(max_length=5)
    block = models.CharField(max_length=5)
    dmin = models.IntegerField()

    class Meta:
        db_table = "enemy"

class enemy_stage(models.Model):
    nome = models.CharField(max_length=150)
    hp = models.IntegerField()
    hp_base = models.IntegerField(blank=True)
    esquiva = models.CharField(max_length=5)
    block = models.CharField(max_length=5)
    dmin = models.IntegerField()
    dresult = models.IntegerField(default=0)

    class Meta:
        db_table = "enemy_stage"

class skill(models.Model):
    nome = models.CharField(max_length=150)
    identificador = models.CharField(max_length=10)
    cd = models.IntegerField()
    cd_corrent = models.IntegerField(default = 0)
    duracao = models.IntegerField()
    duracao_corrent = models.IntegerField(default = 0)
    max_use = models.IntegerField()
    max_use_corrent = models.IntegerField(default = 0)
    fist_turn = models.IntegerField(default = 0)
    dano = models.IntegerField(blank = True)
    bonus_dano = models.IntegerField(null=True, blank = True)
    bonus_cost = models.IntegerField(null=True, blank = True)
    estamina = models.IntegerField(blank = True)
    char = models.ForeignKey('char', on_delete=models.DO_NOTHING,)
    tipo = models.CharField(max_length=50, blank=True)
    reduc = models.IntegerField(default=0)
    item_cost = models.IntegerField(default=0)
    item_cost_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = "skill"

class enemy_skill(models.Model):
    nome = models.CharField(max_length=150)
    cd = models.IntegerField()
    cd_corrent = models.IntegerField(default = 0)
    duracao = models.IntegerField()
    duracao_corrent = models.IntegerField(default = 0) 
    dano = models.IntegerField(blank = True)  
    enemy = models.ForeignKey('enemy', on_delete=models.DO_NOTHING,)
    tipo = models.CharField(max_length=50, blank=True)
    reduc = models.IntegerField(default=0)

    class Meta:
        db_table = "enemy_skill"

class rodada(models.Model):
    turn = models.IntegerField(default = 0)
    
    class Meta:
        db_table = "rodada"

class minion(models.Model):
    nome = models.CharField(max_length=150)
    hp = models.IntegerField()
    base_hp = models.IntegerField(blank=True)
    char = models.ForeignKey('char', on_delete=models.DO_NOTHING,)
    skill = models.ForeignKey('skill', on_delete=models.DO_NOTHING, default=1)

    class Meta:
        db_table = "minion"

class minion_skill(models.Model):
    nome = models.CharField(max_length=150)
    identificador = models.CharField(max_length=10, blank = True)
    cd = models.IntegerField()
    cd_corrent = models.IntegerField(default = 0)
    duracao = models.IntegerField()
    duracao_corrent = models.IntegerField(default = 0) 
    dano = models.IntegerField(blank = True)  
    minion = models.ForeignKey('minion', on_delete=models.DO_NOTHING,)
    tipo = models.CharField(max_length=50, blank=True)
    max_use = models.IntegerField(default = 0)
    max_use_corrent = models.IntegerField(default = 0)
    fist_turn = models.IntegerField(default = 0)
    reduc = models.IntegerField(default=0)

    class Meta:
        db_table = "minion_skill"

class minion_stage(models.Model):
    nome = models.CharField(max_length=150)
    hp = models.IntegerField()
    base_hp = models.IntegerField(blank=True)
    dresult = models.IntegerField(default=0)
    char = models.IntegerField(default=0)
    minion_id = models.IntegerField(default=0)
    skill_id = models.IntegerField(default=0)

    class Meta:
        db_table = "minion_stage"

class debuf(models.Model):
    nome = models.CharField(max_length=150)
    duracao = models.IntegerField()

    class Meta:
        db_table = "debuf"
