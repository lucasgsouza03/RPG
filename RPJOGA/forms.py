from django import forms

class acoes(forms.Form):
    char = forms.CharField()
    esquiva = forms.CharField()
    block = forms.CharField()
    action = forms.CharField()
    dano = forms.IntegerField()
    perda = forms.IntegerField()


    def calc_hit_hp(hp, estamina, dano, dodge, block):
        hp = int(hp)
        estamina = int(estamina)
        dano = int(dano)
        
        if dodge == 's':
            estamina = estamina - 30
            return hp, estamina
        elif block == 's':
            estamina = estamina - 10
            return hp, estamina
        elif dodge == 'n':
            estamina = estamina - 30
            hp  = hp - dano
            estamina = estamina - (dano / 4)
            return hp, estamina
        elif block == 'n':
            estamina = estamina - 10    
            hp  = hp - dano
            estamina = estamina - (dano / 4)
            return hp, estamina
        else:
            hp  = hp - dano
            estamina = estamina - (dano / 4)
            return hp, estamina

    def acao(acao, estamina, perda, forc_vont):
        base = 40
        estamina = int(estamina)
        if perda:
            perda = int(perda)
        forc_vont = int(forc_vont)
        if acao == "atacar":
            estamina = estamina - (perda + base)
            return estamina
        elif acao == "descanso":
            if forc_vont == 6:
                estamina = estamina + 60
            else:
                estamina = estamina + 30
            return estamina

    def turno(estamina, forc_vont):
        forc_vont = int(forc_vont)
        if forc_vont == 6:
            estamina = estamina + 30
            return estamina
        else:
            estamina = estamina + 15
            return estamina

class malun_est(forms.Form):
    nome = forms.CharField()
    forca = forms.IntegerField
    habilidade = forms.IntegerField
    agilidade = forms.IntegerField
    dex = forms.IntegerField
    inteligencia = forms.IntegerField
    forc_vont = forms.IntegerField

    def calc_hp(self, forca, forc_vont):
        base = 200
        forca = int(forca)
        forc_vont = int(forc_vont)
        hp = base + ((forca + 2) ** 2) + ((forc_vont * 3) ** 2)
        return hp

    def calc_estamina(self, forc_vont):
        base = 50
        forc_vont = int(forc_vont)
        estamina = base + ((forc_vont + 10)**2)
        return estamina