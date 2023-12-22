from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from lm_accounts.models import *
from lm_accounts.forms import *

@login_required
def home(request):
    lm_accounts = LMUserAccount.objects.all()
    lm_account_form = LMUserAccountForm()
    context = {
        "home_message":"accounts page",
        "lm_accounts":lm_accounts,
        "lm_account_form":lm_account_form,
    }
    return render(request,'lm_accounts/home.html',context)

@login_required
def createAccount(request):
    if request.method == "POST":
        ign = request.POST.get("IGN")
        reset_time = request.POST.get("reset_time")
        email = request.POST.get("email")
        provider = request.POST.get("provider")
        lm_user = LMUserAccount.objects.create(
            IGN=ign,
            reset_time=reset_time,
            email=email,
            provider=provider,
        )
        LMUserResearch.objects.create(
            account = lm_user
        )
        LMUserBag.objects.create(
            account_id = lm_user
        )
        return redirect("home-accounts")
    
def readAccount(request,pk):
    lm_account = get_object_or_404(LMUserAccount, id=pk)
    lm_user_bag = LMUserBag.objects.get(account_id=lm_account)
    lm_user_research = LMUserResearch.objects.get(account_id=lm_account)
    lm_user_bag_chest = LMUserBagChest.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_unique = LMUserBagUnique.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_speed_up = LMUserBagSpeedUp.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_combat = LMUserBagCombat.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_resources = LMUserBagResources.objects.filter(bag_id=lm_user_bag)
    lm_user_research_economy = LMUserResearchEconomy.objects.filter(research=lm_user_research)
    lm_user_research_defense = LMUserResearchDefense.objects.filter(research=lm_user_research)
    lm_user_research_military = LMUserResearchMilitary.objects.filter(research=lm_user_research)
    lm_user_research_monster_hunt = LMUserResearchMonsterHunt.objects.filter(research=lm_user_research)
    lm_user_research_upgrade_defenses = LMUserResearchUpgradeDefenses.objects.filter(research=lm_user_research)
    
    lm_user_bag_chest_form = LMUserBagChestForm()
    lm_user_bag_unique_form = LMUserBagUniqueForm()
    lm_user_bag_speed_up_form = LMUserBagSpeedUpForm()
    lm_user_bag_combat_form = LMUserBagCombatForm()
    lm_user_bag_resources_form = LMUserBagResourcesForm()
    lm_user_research_economy_form = LMUserResearchEconomyForm()
    lm_user_research_defense_form = LMUserResearchDefenseForm()
    lm_user_research_military_form = LMUserResearchMilitaryForm()
    lm_user_research_monster_hunt_form = LMUserResearchMonsterHuntForm()
    lm_user_research_upgrade_defenses_form = LMUserResearchUpgradeDefensesForm()
    context = {
        "lm_account":lm_account,
        
        "lm_user_bag_chest":lm_user_bag_chest,
        "lm_user_bag_chest_form":lm_user_bag_chest_form,
        "lm_user_bag_unique":lm_user_bag_unique,
        "lm_user_bag_combat":lm_user_bag_combat,
        "lm_user_bag_resources":lm_user_bag_resources,
        "lm_user_bag_unique_form":lm_user_bag_unique_form,
        "lm_user_bag_speed_up":lm_user_bag_speed_up,
        "lm_user_bag_speed_up_form":lm_user_bag_speed_up_form,
        "lm_user_bag_combat_form":lm_user_bag_combat_form,
        "lm_user_bag_resources_form":lm_user_bag_resources_form,

        "lm_user_research_economy":lm_user_research_economy,
        "lm_user_research_economy_form":lm_user_research_economy_form,
        "lm_user_research_defense":lm_user_research_defense,
        "lm_user_research_defense_form":lm_user_research_defense_form,
        "lm_user_research_military":lm_user_research_military,
        "lm_user_research_military_form":lm_user_research_military_form,
        "lm_user_research_monster_hunt":lm_user_research_monster_hunt,
        "lm_user_research_monster_hunt_form":lm_user_research_monster_hunt_form,
        "lm_user_research_upgrade_defenses":lm_user_research_upgrade_defenses,
        "lm_user_research_upgrade_defenses_form":lm_user_research_upgrade_defenses_form,
    }
    return render(request,'lm_accounts/lm_account_details.html',context)
    
def updateAccount(request,pk):
    lm_account = get_object_or_404(LMUserAccount, id=pk)
    lm_account_form = LMUserAccountForm(instance=lm_account)
    if request.method == 'POST':
        ign = request.POST.get("IGN")
        reset_time = request.POST.get("reset_time")
        email = request.POST.get("email")
        provider = request.POST.get("provider")
        lm_account.IGN = ign
        lm_account.reset_time = reset_time
        lm_account.email = email
        lm_account.provider = provider
        lm_account.save()
        return redirect("home-accounts")
    context = {
        "home_message":"accounts page",
        "lm_account":lm_account,
        "lm_account_form":lm_account_form,
    }
    return render(request,'lm_accounts/update_account.html',context)

def deleteAcoount(request,pk):
    lm_account = LMUserAccount.objects.get(id=pk)
    lm_account.delete()
    return redirect("home-accounts")
