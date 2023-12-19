from django.shortcuts import render, redirect, get_object_or_404
from lm_accounts.models import *
from lm_accounts.forms import *


def createResearchEconomy(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_research = LMUserResearch.objects.get(account=lm_account)
        LMUserResearchEconomy.objects.create(
            name=name,
            level=level,
            research=lm_research,
        )
        return redirect("read-lm-account", pk=account_id)
    
def updateResearchEconomy(request,pk):
    lm_user_research_economy = get_object_or_404(LMUserResearchEconomy, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_economy.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_economy_form = LMUserResearchEconomyForm(instance=lm_user_research_economy)
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        lm_user_research_economy.name = name
        lm_user_research_economy.level = level
        lm_user_research_economy.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_research_economy_form":lm_user_research_economy_form,
    }
    return render(request,'lm_accounts/lm_research/lm_research_economy_update.html',context)

def deleteResearchEconomy(request,pk):
    lm_user_research_economy = get_object_or_404(LMUserResearchEconomy, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_economy.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_economy.delete()
    return redirect("read-lm-account", pk=lm_account.id)

def createResearchDefense(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_research = LMUserResearch.objects.get(account=lm_account)
        LMUserResearchDefense.objects.create(
            name=name,
            level=level,
            research=lm_research,
        )
        return redirect("read-lm-account", pk=account_id)

def updateResearchDefense(request,pk):
    lm_user_research_defense = get_object_or_404(LMUserResearchDefense, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_defense.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_defense_form = LMUserResearchDefenseForm(instance=lm_user_research_defense)
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        lm_user_research_defense.name = name
        lm_user_research_defense.level = level
        lm_user_research_defense.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_research_defense_form":lm_user_research_defense_form,
    }
    return render(request,'lm_accounts/lm_research/lm_research_defense_update.html',context)

def deleteResearchDefense(request,pk):
    lm_user_research_defense = get_object_or_404(LMUserResearchDefense, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_defense.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_defense.delete()
    return redirect("read-lm-account", pk=lm_account.id)

def createResearchMilitary(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_research = LMUserResearch.objects.get(account=lm_account)
        LMUserResearchMilitary.objects.create(
            name=name,
            level=level,
            research=lm_research,
        )
        return redirect("read-lm-account", pk=account_id)

def updateResearchMilitary(request,pk):
    lm_user_research_military = get_object_or_404(LMUserResearchMilitary, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_military.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_military_form = LMUserResearchMilitaryForm(instance=lm_user_research_military)
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        lm_user_research_military.name = name
        lm_user_research_military.level = level
        lm_user_research_military.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_research_military_form":lm_user_research_military_form,
    }
    return render(request,'lm_accounts/lm_research/lm_research_military_update.html',context)

def deleteResearchMilitary(request,pk):
    lm_user_research_military = get_object_or_404(LMUserResearchMilitary, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_military.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_military.delete()
    return redirect("read-lm-account", pk=lm_account.id)

def createResearchMonsterHunt(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_research = LMUserResearch.objects.get(account=lm_account)
        LMUserResearchMonsterHunt.objects.create(
            name=name,
            level=level,
            research=lm_research,
        )
        return redirect("read-lm-account", pk=account_id)

def updateResearchMonsterHunt(request,pk):
    lm_user_research_monster_hunt = get_object_or_404(LMUserResearchMonsterHunt, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_monster_hunt.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_monster_hunt_form = LMUserResearchMonsterHuntForm(instance=lm_user_research_monster_hunt)
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        lm_user_research_monster_hunt.name = name
        lm_user_research_monster_hunt.level = level
        lm_user_research_monster_hunt.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_research_monster_hunt_form":lm_user_research_monster_hunt_form,
    }
    return render(request,'lm_accounts/lm_research/lm_research_monster_hunt_update.html',context)

def deleteResearchMonsterHunt(request,pk):
    lm_user_research_monster_hunt = get_object_or_404(LMUserResearchMonsterHunt, id=pk)
    lm_user_research = get_object_or_404(LMUserResearch, id=lm_user_research_monster_hunt.research.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.account.id)
    lm_user_research_monster_hunt.delete()
    return redirect("read-lm-account", pk=lm_account.id)