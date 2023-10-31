from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import LMAccount
from lm_accounts.models import LMUserAccount,LMUserBag,LMUserBagChest,LMUserBagCombat,LMUserBagResources,LMUserBagSpeedUp,LMUserBagUnique
from lm_accounts.forms import LMUserAccountForm,LMUserBagChestForm

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
        LMUserAccount.objects.create(
            IGN=ign,
            reset_time=reset_time,
            email=email,
            provider=provider,
        )
        
        return redirect("home-accounts")

def createBagChest(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        count = request.POST.get("count")
        bag_id = request.POST.get("bag_id")
        account_id = request.POST.get("pk")
        lm_bag = LMUserBag.objects.get(id=bag_id)
        LMUserBagChest.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        print("nya")
        return redirect("read-lm-account", pk=account_id)
    
def readAccount(request,pk):
    lm_account = get_object_or_404(LMUserAccount, id=pk)
    lm_user_bag = LMUserBag.objects.get(account_id=lm_account)
    lm_user_bag_chest = LMUserBagChest.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_chest_form = LMUserBagChestForm()
    context = {
        "lm_account":lm_account,
        "lm_user_bag_chest":lm_user_bag_chest,
        "lm_user_bag_chest_form":lm_user_bag_chest_form,
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