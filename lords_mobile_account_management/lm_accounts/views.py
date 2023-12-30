from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from lm_accounts.models import *
from lm_accounts.forms import *
from lm_accounts.utils import checkModel,checkForm

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
    lm_user_research_upgrade_military = LMUserResearchUpgradeMilitary.objects.filter(research=lm_user_research)
    lm_user_research_army_leadership = LMUserResearchArmyLeadership.objects.filter(research=lm_user_research)
    lm_user_research_military_command = LMUserResearchMilitaryCommand.objects.filter(research=lm_user_research)
    lm_user_research_familiar = LMUserResearchFamiliar.objects.filter(research=lm_user_research)
    lm_user_research_familiar_battles = LMUserResearchFamiliarBattles.objects.filter(research=lm_user_research)
    lm_user_research_sigil = LMUserResearchSigil.objects.filter(research=lm_user_research)
    lm_user_research_wonder_battles = LMUserResearchWonderBattles.objects.filter(research=lm_user_research)
    lm_user_research_gear = LMUserResearchGear.objects.filter(research=lm_user_research)
    lm_user_research_advanced_wonder_battles = LMUserResearchAdvancedWonderBattles.objects.filter(research=lm_user_research)
    
    
    context = {
        "lm_account":lm_account,
        
        "lm_user_bag_chest":lm_user_bag_chest,
        "lm_user_bag_unique":lm_user_bag_unique,
        "lm_user_bag_combat":lm_user_bag_combat,
        "lm_user_bag_resources":lm_user_bag_resources,
        "lm_user_bag_speed_up":lm_user_bag_speed_up,

        "lm_user_research_economy":lm_user_research_economy,
        "lm_user_research_defense":lm_user_research_defense,
        "lm_user_research_military":lm_user_research_military,
        "lm_user_research_monster_hunt":lm_user_research_monster_hunt,
        "lm_user_research_upgrade_defenses":lm_user_research_upgrade_defenses,
        "lm_user_research_upgrade_military":lm_user_research_upgrade_military,
        "lm_user_research_army_leadership":lm_user_research_army_leadership,
        "lm_user_research_military_command":lm_user_research_military_command,
        "lm_user_research_familiar":lm_user_research_familiar,
        "lm_user_research_familiar_battles":lm_user_research_familiar_battles,
        "lm_user_research_sigil":lm_user_research_sigil,
        "lm_user_research_wonder_battles":lm_user_research_wonder_battles,
        "lm_user_research_gear":lm_user_research_gear,
        "lm_user_research_advanced_wonder_battles":lm_user_research_advanced_wonder_battles,
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
