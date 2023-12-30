from django.shortcuts import render, redirect, get_object_or_404
from lm_accounts.models import *
from lm_accounts.forms import *
from lm_accounts.utils import checkModel,checkForm

def createResearch(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        account_id = request.POST.get("pk")
        research_type = request.POST.get("research_type")
        research_type = checkModel(research_type, 'research')
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        research = LMUserResearch.objects.get(account=lm_account)
        research_type.objects.create(
            name=name,
            level=level,
            research=research,
        )
        return redirect("read-lm-account", pk=account_id)

def updateResearch(request,type,pk):
    research_type = checkModel(type, 'research')
    lm_user_research = get_object_or_404(research_type, id=pk)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.research.account.id)
    form_type = checkForm(type, 'research')
    lm_user_research_form = form_type(instance = lm_user_research)
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        lm_user_research.name = name
        lm_user_research.level = level
        lm_user_research.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_research_form":lm_user_research_form,
    }
    return render(request,'lm_accounts/lm_research/lm_research_update.html',context)

def deleteResearch(request,type,pk):
    research_type = checkModel(type, 'research')
    lm_user_research = get_object_or_404(research_type, id=pk)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_research.research.account.id)
    lm_user_research.delete()
    return redirect("read-lm-account", pk=lm_account.id)
