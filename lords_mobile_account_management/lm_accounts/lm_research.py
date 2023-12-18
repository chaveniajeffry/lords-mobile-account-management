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