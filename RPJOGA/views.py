from django.shortcuts import render
from django.http import HttpResponseRedirect
from RPJOGA.models import *
from RPJOGA.forms import acoes, malun_est
from RPJOGA.src.dado import dado
import random

# Create your views here.

def perfil(request):
    if request.POST:
        form = acoes(request.POST)
        nome = request.POST.get("char")
        minionator = request.POST.get("minion")
        Esquiva = request.POST.get("esquiva")
        Block = request.POST.get("block")
        Action = request.POST.get("action")
        Perda_de_estamina = request.POST.get("perda")
        Dano = request.POST.get("dano")
        Cura = request.POST.get("cura")
        turno = request.POST.get("EndTurn")
        restore = request.POST.get("FullRestore")
        aoe = request.POST.get("aoe")
        start = request.POST.get("Start")
        end = request.POST.get("End")
        cd = request.POST.get("RestoreCD")
        estamina = request.POST.get("RestoreEstamina")
        reduc = request.POST.get("reduc") 

        if nome:
            dude = char.objects.get(nome=nome)
            dude.reduc = reduc
            dude.save()
        elif minionator:
            dude = minion_stage.objects.get(id=minionator)
            Block = ""
            Esquiva = ""
        else:
            dude = char.objects.all()
        if Action:
            estamina = acoes.acao(Action, dude.estamina, Perda_de_estamina, dude.forc_vont)
            if estamina > dude.base_estamina:
                estamina = dude.base_estamina
            elif estamina < 0:
                estamina = 0
            dude.estamina = estamina
            dude.save()
            if Action == "atacar":
                stam = int(Perda_de_estamina) + 30
                msg = str(dude.nome)+" performa a ação "+str(Action)+" e gasta "+str(stam)
                log.objects.create(tipo="ACTION", mensagem=msg)
            else:
                msg = str(dude.nome)+" performa "+str(Action)+" e recupera sua estamina"
                log.objects.create(tipo="ACTION", mensagem=msg)
        elif aoe:
            if int(aoe) >= 0:
                for i in dude:
                    i.hp = i.hp - int(aoe)
                    i.estamina = i.estamina - (int(aoe)/4)
                    if i.hp > i.base_hp:
                        i.hp = i.base_hp
                    if i.estamina > i.base_estamina:
                        i.estamina = i.base_estamina
                    i.save()
            elif int(aoe) < 0:
                for i in dude:
                    i.hp = i.hp - int(aoe)
                    if i.hp > i.base_hp:
                        i.hp = i.base_hp
                    i.save()
        elif turno:
            skills = skill.objects.all()
            minion_skills = minion_skill.objects.all()
            debuff = debuf.objects.filter(id=1)
            for i in debuff:
                if i.duracao > 0:
                    i.duracao = i.duracao - 1
                    i.save()
            for i in skills:
                if i.duracao_corrent == 20:
                    m = minion_stage.objects.filter(skill_id=i.id)
                    vali = None
                    for j in m:
                        if j.nome != None:
                            vali = "minion"
                    if vali == None:
                        i.duracao_corrent = 0
                        i.cd_corrent = i.cd
                        i.save()
                elif i.duracao > 0 or i.duracao < 20:
                    if i.fist_turn == 0:
                        if i.duracao_corrent > 1:
                            current_duracao = i.duracao_corrent - 1
                            i.duracao_corrent = current_duracao
                            i.save()
                        elif i.duracao_corrent == 1:
                            current_duracao = i.duracao_corrent - 1
                            i.duracao_corrent = current_duracao
                            if i.tipo == "summon":
                                minion_stage.objects.get(skill_id=i.id).delete()
                            i.cd_corrent = i.cd
                            i.save()
                        elif i.duracao_corrent == 0 and i.cd_corrent > 0:
                            current_cd = i.cd_corrent - 1
                            i.cd_corrent = current_cd
                            i.save()
                        
                    elif i.fist_turn == 1:
                        i.fist_turn = 0
                        i.save()
                    

                elif i.cd_corrent > 0:  
                    if i.fist_turn == 0:  
                        current_cd = i.cd_corrent - 1
                        i.cd_corrent = current_cd
                        i.save()
                    elif i.fist_turn == 1:
                        i.fist_turn = 0
                        i.save()
                        
            for i in minion_skills:
                if i.duracao > 0:
                    if i.fist_turn == 0:
                        if i.duracao_corrent > 1:
                            current_duracao = i.duracao_corrent - 1
                            i.duracao_corrent = current_duracao
                            i.save()
                        elif i.duracao_corrent == 1:
                            current_duracao = i.duracao_corrent - 1
                            i.duracao_corrent = current_duracao
                            i.cd_corrent = i.cd
                            i.save()
                        elif i.duracao_corrent == 0 and i.cd_corrent > 0:
                            current_cd = i.cd_corrent - 1
                            i.cd_corrent = current_cd
                            i.save()
                    elif i.fist_turn == 1:
                        i.fist_turn = 0
                        i.save()
                elif i.cd_corrent > 0:  
                    if i.fist_turn == 0:  
                        current_cd = i.cd_corrent - 1
                        i.cd_corrent = current_cd
                        i.save()
                    elif i.fist_turn == 1:
                        i.fist_turn = 0
                        i.save()                            
            for i in dude:
                estamina = acoes.turno(i.estamina, i.forc_vont)
                if estamina > i.base_estamina:
                    estamina = i.base_estamina
                i.estamina = estamina
                i.save()
            msg = "Fim de turno--------------------------------------------------------------------------------------------------------------------------"
            log.objects.create(tipo="ACTION", mensagem=msg)
        elif restore:
            skills = skill.objects.all()
            minions = minion_stage.objects.all().delete()
            minion_skills = minion_skill.objects.all()
            debuff = debuf.objects.filter(id=1)
            for i in debuff:
                i.duracao = 0
                i.save()
            for i in dude:
                i.hp = i.base_hp
                i.estamina = i.base_estamina
                i.save()
            for i in skills:
                i.cd_corrent = 0
                i.duracao_corrent = 0
                i.fist_turn = 0
                i.max_use_corrent = i.max_use
                i.save()
            for i in minion_skills:
                i.cd_corrent = 0
                i.duracao_corrent = 0
                i.fist_turn = 0
                i.max_use_corrent = i.max_use
                i.save()
        elif cd:
            skills = skill.objects.filter(char_id=dude.id)
            mini = minion.objects.get(char_id=dude.id)
            minion_skills = minion_skill.objects.filter(minion_id=mini.id)
            for i in skills:
                i.cd_corrent = 0
                i.duracao_corrent = 0
                i.fist_turn = 0
                i.max_use_corrent = i.max_use
                i.save()
            for i in minion_skills:
                i.cd_corrent = 0
                i.duracao_corrent = 0
                i.fist_turn = 0
                i.max_use_corrent = i.max_use
                i.save()
        elif estamina != "0" and estamina != None:
            dude.estamina = dude.estamina + int(estamina)
            if dude.estamina > dude.base_estamina:
                dude.estamina = dude.base_estamina
            dude.save()
        elif start:
            msg = "Início da batalha==================================================================================="
            log.objects.create(tipo="BLOCK", mensagem=msg)
        elif end:
            msg = "Fim da batalha===================================================================================="
            log.objects.create(tipo="BLOCK", mensagem=msg)
        elif Block != "":
            tupla = acoes.calc_hit_hp(dude.hp, dude.estamina, Dano, Esquiva, Block)
            estamina = tupla[1]
            if estamina < 0:
                estamina = 0
            hp = tupla[0]
            dude.estamina = estamina
            dude.hp = hp
            dude.save()
            if Block == "s":
                msg = str(dude.nome)+" efetua block com sucesso"
                log.objects.create(tipo="BLOCK", mensagem=msg)
            else:
                msg = str(dude.nome)+" falha ao efetuar o block e toma "+str(Dano)+" de dano"
                log.objects.create(tipo="BLOCK", mensagem=msg)
        elif Esquiva != "":
            tupla = acoes.calc_hit_hp(dude.hp, dude.estamina, Dano, Esquiva, Block)
            estamina = tupla[1]
            if estamina < 0:
                estamina = 0
            hp = tupla[0]
            dude.estamina = estamina
            dude.hp = hp
            dude.save()
            if Esquiva == "s":
                msg = str(dude.nome)+" efetua esquiva com sucesso"
                log.objects.create(tipo="ESQUIVA", mensagem=msg)
            else:
                msg = str(dude.nome)+" falha ao efetuar a esquiva e toma "+str(Dano)+" de dano"
                log.objects.create(tipo="ESQUIVA", mensagem=msg)
        elif Dano != "0":
            if minionator:
                dude.hp = dude.hp - int(Dano)
                dude.save()
                if dude.hp <= 0:
                    info = minion_stage.objects.get(id=dude.id)
                    m_skill = skill.objects.get(id=info.skill_id)
                    m_skill.duracao_corrent = 0
                    m_skill.cd_corrent = m_skill.cd
                    m_skill.save()
                    info.delete()
                    msg = str(dude.nome)+" morre ao receber "+str(Dano)+" de dano"
                    log.objects.create(tipo="DAMAGE", mensagem=msg)
                else:
                    msg = str(dude.nome)+" sofre ataque do inimigo e toma "+str(Dano)+" de dano"
                    log.objects.create(tipo="DAMAGE", mensagem=msg)
            else:
                tupla = acoes.calc_hit_hp(dude.hp, dude.estamina, Dano, Esquiva, Block)
                estamina = tupla[1]
                if estamina < 0:
                    estamina = 0
                hp = tupla[0]
                dude.estamina = estamina
                dude.hp = hp
                dude.save()
                msg = str(dude.nome)+" sofre ataque do inimigo e toma "+str(Dano)+" de dano"
                log.objects.create(tipo="DAMAGE", mensagem=msg)
        elif Cura != "0":
            hp = dude.hp + int(Cura)
            if hp > dude.base_hp:
                hp = dude.base_hp
            dude.hp = hp
            dude.save()
            msg = str(dude.nome)+" recebe uma cura de "+str(Cura)+" de HP"
            log.objects.create(tipo="HEAL", mensagem=msg)
    else:
        form = acoes()

    contexto = {
        "perfis":char.objects.all(),
        "minions":minion_stage.objects.all(),
        "form": form
    }
    return render(request, "perfil.html", contexto)

def perfil_inimigo(request):
    if request.POST:
        Dano = request.POST.get("dano")
        Cura = request.POST.get("cura")
        load = request.POST.get("load")
        num = request.POST.get("num")
        inimigo = request.POST.get("inimigo")
        ident = request.POST.get("ident")
        n = request.POST.get("dado")
        if n:
            stage = enemy_stage.objects.get(id=ident)
            n = int(n)
            result = random.randrange(1,n+1)
            enemy_stage.objects.filter(id=ident).update(dresult=result)
            msg = str(stage.nome)+" rola um D"+str(n)+" e tira "+str(result)
            log.objects.create(tipo="DICE", mensagem=msg)
        elif load:
            load_enemy = enemy.objects.get(id=int(load))
            if num:
                nome_enemy = load_enemy.nome + str("("+num+")")
                enemy_stage.objects.create(nome=nome_enemy, hp=load_enemy.hp, hp_base=load_enemy.hp_base, esquiva=load_enemy.esquiva, block=load_enemy.block, dmin=load_enemy.dmin)
            else:
                enemy_stage.objects.create(nome=load_enemy.nome, hp=load_enemy.hp, hp_base=load_enemy.hp_base, esquiva=load_enemy.esquiva, block=load_enemy.block, dmin=load_enemy.dmin)
        elif Dano != "0":
            stage = enemy_stage.objects.get(id=inimigo)
            stage.hp = stage.hp - int(Dano)
            if stage.hp <= 0:
                stage = enemy_stage.objects.filter(id=inimigo).delete()

            else:
                stage.save()
        elif Cura != "0":
            stage = enemy_stage.objects.get(id=inimigo)
            stage.hp = stage.hp + int(Cura)
            if stage.hp > stage.hp_base:
                stage.hp = stage.hp_base
                stage.save()
            else:
                stage.save()
    contexto = {
        "enemys":enemy.objects.all(),
        "perfis":enemy_stage.objects.all(),
    }
    return render(request, "perfil_inimigo.html", contexto)

def create_char(request):
    if request.POST:
        form = malun_est(request.POST) 
        nome = request.POST.get("nome")
        identificador= request.POST.get("identificador")
        forca = request.POST.get("forca")
        habilidade = request.POST.get("habilidade")
        agilidade = request.POST.get("agilidade")
        dex = request.POST.get("dex")
        inteligencia = request.POST.get("inteligencia")
        forc_vont = request.POST.get("forc_vont")
        dmin = request.POST.get("dmin")
        hp = form.calc_hp(forca, forc_vont)
        estamina = form.calc_estamina(forc_vont)
        dcrit = form.calc_crit(dmin)

        if (int(forca)+int(habilidade)+int(agilidade)+int(dex)+int(inteligencia)+int(forc_vont)) == 17:
            dude = char.objects.create(nome=nome, identificador=identificador, forca=forca, habilidade=habilidade, agilidade=agilidade, dex=dex, inteligencia=inteligencia, forc_vont=forc_vont, hp=hp, estamina=estamina, base_hp=hp, base_estamina=estamina, dmin=dmin, dcrit=dcrit)
            dude.save()
        
    else:
        form = malun_est()

    contexto = {
        "form": form
    }
    return render(request, "create_char.html", contexto)

def create_skill(request):
    if request.POST: 
        nome = request.POST.get("nome")
        identificador = request.POST.get("identificador")
        cd = request.POST.get("cd")
        duracao = request.POST.get("duracao")
        reduc = request.POST.get("reduc")
        dano = request.POST.get("dano")
        dano_bonus = request.POST.get("dano_bonus")
        cost_bonus = request.POST.get("cost_bonus")
        aliado = request.POST.get("aliado")
        inimigo = request.POST.get("inimigo")
        minions = request.POST.get("minion")
        tipo = request.POST.get("tipo")
        max_use = request.POST.get("max_use")
        estamina = request.POST.get("estamina")
        if aliado:
            skill.objects.create(nome=nome, identificador=identificador, cd=cd, duracao=duracao, reduc=reduc, dano=dano, char_id=aliado, tipo=tipo, max_use=max_use, max_use_corrent=max_use, estamina=estamina, bonus_dano=dano_bonus, bonus_cost=cost_bonus)
        elif inimigo:
            enemy_skill.objects.create(nome=nome, cd=cd, duracao=duracao, reduc=reduc, dano=dano, enemy_id=inimigo)
        elif minions:
            minion_skill.objects.create(nome=nome, identificador=identificador, cd=cd, duracao=duracao, reduc=reduc, dano=dano, minion_id=minions, tipo=tipo)

    contexto = {
        "chars":char.objects.all(),
        "enemys":enemy.objects.all(),
        "minions":minion.objects.all(),
    }
    return render(request, "create_skill.html", contexto)

def create_enemy(request):
    if request.POST: 
        nome = request.POST.get("nome")
        hp = request.POST.get("hp")
        esquiva = request.POST.get("esquiva")
        block = request.POST.get("block")
        dmin = request.POST.get("dmin")
        dude = enemy.objects.create(nome=nome, hp=hp, hp_base=hp, esquiva=esquiva, block=block, dmin=dmin)
        dude.save()
    return render(request, "create_enemy.html")

def create_minions(request):
    if request.POST: 
        nome = request.POST.get("nome")
        hp = request.POST.get("hp")
        person = request.POST.get("char")
        habili = request.POST.get("skill")
        dude = minion.objects.create(nome=nome, hp=hp, base_hp=hp, char_id=person, skill_id=habili)
        dude.save()
    contexto = {
        "chars":char.objects.all(),
        "skills":skill.objects.all(),
    }
    return render(request, "create_minions.html", contexto)

def detalhes(request, identificador):
    perso = char.objects.get(identificador=identificador)
    skills = skill.objects.filter(char_id__id=perso.id)
    minions = minion_stage.objects.filter(char=perso.id)
    minion_skills = minion_skill.objects.all()
    vali = None
    for i in minions:
        if i.nome != None:
            vali = "minion"
    if request.POST:
        n = request.POST.get("dado")
        pala = request.POST.get("skill")
        reduc = request.POST.get("reduc")
        passiva = request.POST.get("passiva")
        minion_action = request.POST.get("minion_action")
        infeliz = request.POST.get("infeliz")
        ativa = request.POST.get("ativa")
        bonus = request.POST.get("bonus")
        debuff = request.POST.get("debuf")
        quickskill = request.POST.get("quickskill")
        hab = ""
        if pala != None:
            palas = pala.split(",")
            hab = palas[0]
            identify = palas[1]
        if n:
            n = int(n)
            result = random.randrange(1,n+1)
            msg = str(perso.nome)+" rola um D"+str(n)+" e tira "+str(result)
            log.objects.create(tipo="DICE", mensagem=msg)
        else:
            result = 0
        if ativa:
            s = skill.objects.get(id=int(ativa))
            inv = skill.objects.get(nome="Summone Ignis")
            if s.nome == "Reverberação Calcinante" and inv.cd_corrent > 0:
                inv.cd_corrent = inv.cd_corrent - s.reduc
                inv.save()
        elif hab:
            habili = skill.objects.get(id=int(hab))
            if minion_action:
                habili = minion_skill.objects.get(id=int(hab))
                if habili.nome == "Martírio Lampejante":
                    mini = minion_stage.objects.get(char=1)
                    minion_s = minion_skill.objects.filter(minion_id=int(infeliz))
                    c = (mini.hp/100)*50
                    perso.hp = perso.hp + int(c)
                    perso.save()
                    mini.delete()
                    for i in minion_s:
                        i.cd_corrent = 0
                        i.duracao_corrent = 0
                if habili.max_use != 0:
                    habili.max_use_corrent = habili.max_use_corrent - 1
                    habili.save()
                if habili.duracao:
                    if habili.duracao_corrent == 0 and habili.cd_corrent == 0:
                        minion_skill.objects.filter(id=int(hab)).update(cd_corrent=habili.duracao,duracao_corrent=habili.duracao,fist_turn=1)
                else:
                    porra = minion_skill.objects.filter(identificador=identify)
                    for por in porra:
                        por.cd_corrent = habili.cd
                        por.fist_turn = 1
                        por.save()
            elif habili.estamina <= perso.estamina:
                if habili.nome == "Pika das Galaxias":
                    perso.estamina = 0
                    perso.save()
                if habili.nome == "Maldição Sombria":
                    debuf.objects.filter(id=1).update(duracao=2)
                
                elif habili.bonus_cost != 0 and perso.nome == 'Mandrake Satawin':
                    perso.hp = perso.hp - habili.bonus_cost
                    perso.save()
                perso.estamina = perso.estamina - habili.estamina
                perso.save()
                dmin = perso.dmin - perso.reduc
                if reduc:
                    dmin = dmin - int(reduc)
                else:
                    dmin = dmin - habili.reduc
                if result >= dmin:
                    if habili.tipo == "summon":
                        load_minion = minion.objects.get(skill_id__id=habili.id)
                        minion_stage.objects.create(nome=load_minion.nome, hp=load_minion.hp, base_hp=load_minion.base_hp, char=perso.id, minion_id=load_minion.id, skill_id=load_minion.skill_id)
                    if habili.max_use != 0:
                        habili.max_use_corrent = habili.max_use_corrent - 1
                        habili.save()
                    if habili.duracao:
                        if habili.duracao_corrent == 0 and habili.cd_corrent == 0:
                            skill.objects.filter(id=int(hab)).update(cd_corrent=habili.duracao,duracao_corrent=habili.duracao,fist_turn=1)                        
                    else:
                        porra = skill.objects.filter(identificador=identify)
                        for por in porra:
                            por.cd_corrent = habili.cd
                            por.fist_turn = 1
                            por.save() 
                    if result >= perso.dcrit:
                        habili.dano = habili.dano * 2                                   
                    if habili.dano < 0:
                        if habili.nome == "Cura Elfica":
                            party = char.objects.all()
                            cura = int(abs(habili.dano))
                            for dude in party:
                                hp = dude.hp + cura
                                if hp > dude.base_hp:
                                    hp = dude.base_hp
                                dude.hp = hp
                                dude.save()
                        msg = str(perso.nome)+" teve sucesso ao utilizar "+str(habili.nome)+"(Cura: "+str(abs(habili.dano))+")"
                    elif bonus:
                        db = habili.dano + habili.bonus_dano
                        if perso.nome == "Mardek Dragneel":
                            m = minion_stage.objects.filter(char=perso.id)
                            for i in m:
                                if i.hp > habili.bonus_cost:
                                    i.hp = i.hp - habili.bonus_cost
                                    i.save()
                                    if debuff:
                                        db = db * 2
                                        debuf.objects.filter(id=int(debuff)).update(duracao=0)
                                    msg = str(perso.nome)+" teve sucesso ao utilizar "+str(habili.nome)+"(Dano: "+str(db)+")"
                                else:    
                                    log.objects.create(tipo="ERROR", mensagem="Invocação no contem vida suficiente para utilizar o bônus da Skill "+ habili.nome)
                    else:
                        if debuff:
                            if perso.nome == 'Mandrake Satawin' and reduc != None:
                                habili.dano = habili.dano * 3
                                print(habili.dano)
                            else:
                                habili.dano = habili.dano * 2
                                print(habili.dano)
                            debuf.objects.filter(id=int(debuff)).update(duracao=0)
                        msg = str(perso.nome)+" teve sucesso ao utilizar "+str(habili.nome)+"(Dano: "+str(habili.dano)+")"
                        
                    log.objects.create(tipo="SKILL", mensagem=msg)
                elif result < dmin:
                    if habili.max_use != 0:
                        habili.max_use_corrent = habili.max_use_corrent - 1
                        habili.save()
                    if bonus:
                        m = minion_stage.objects.filter(char=perso.id)
                        for i in m:
                            i.hp = i.hp - habili.bonus_cost
                            i.save()
                    skill.objects.filter(id=int(hab)).update(cd_corrent=habili.cd,fist_turn=1)
                    msg = str(perso.nome)+" falha ao utilizar "+str(habili.nome)
                    log.objects.create(tipo="SKILL", mensagem=msg)
            else:
                log.objects.create(tipo="ERROR", mensagem="Estaminha insuficiente para utilizar a Skill "+ habili.nome)
        minions = minion_stage.objects.filter(char=perso.id)
        for i in minions:
            if i.nome != None:
                vali = "minion"
            
        contexto = {
            "resultado": result,
            "perfil": perso,
            "invent": invent.objects.filter(char_id__id=perso.id),
            "skills": skills,
            "minions": minions,
            "minion_skills": minion_skill.objects.all(),
            "vali": vali,
            "debufs": debuf.objects.all(),
        }
    else:
        contexto = {
            "resultado": 0,
            "perfil": perso,
            "invent": invent.objects.filter(char_id__id=perso.id),
            "skills": skills,
            "minions": minions,
            "minion_skills": minion_skills,
            "vali": vali,
            "debufs": debuf.objects.all(),
        }
    return render(request, "detalhes.html", contexto)

def logs(request):
    contexto = {
        "log": log.objects.all().order_by('-id')
    }
    return render(request, "log.html", contexto)

def invent_manage(request):
    nome = request.POST.get("nome")
    qtd = request.POST.get("qtd")
    nome = request.POST.get("nome")
    update = request.POST.get("update")
    delete = request.POST.get("delete")
    new = request.POST.get("new")

    if request.POST:
        if update:
            invent.objects.filter(id=update).update(qtd=qtd)
        elif delete:
            invent.objects.filter(id=delete).delete()
        elif new and nome and qtd:
            dude = char.objects.get(nome=new)
            invent.objects.create(qtd=qtd, nome=nome, char_id=dude.id)
        contexto = {
            "chars": char.objects.all(),
            "items": invent.objects.all(),
        }
    else:
        contexto = {
            "chars": char.objects.all(),
            "items": invent.objects.all(),
        }
    return render(request, "invent_manage.html", contexto)

def char_index(request):
    contexto = {
        'chars': char.objects.all(),
    }
    return render(request, "char.html", contexto)

def pandora(request):
    return render(request, "index.html")