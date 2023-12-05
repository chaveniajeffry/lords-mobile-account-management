from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import LMAccount
from lm_accounts.models import LMUserAccount,LMUserBag,LMUserBagChest,LMUserBagCombat,LMUserBagResources,LMUserBagSpeedUp,LMUserBagUnique
from lm_accounts.forms import LMUserAccountForm,LMUserBagChestForm, LMUserBagUniqueForm

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
        LMUserBag.objects.create(
            account_id = lm_user
        )
        return redirect("home-accounts")
    
def readAccount(request,pk):
    lm_account = get_object_or_404(LMUserAccount, id=pk)
    lm_user_bag = LMUserBag.objects.get(account_id=lm_account)
    lm_user_bag_chest = LMUserBagChest.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_unique = LMUserBagUnique.objects.filter(bag_id=lm_user_bag)
    lm_user_bag_chest_form = LMUserBagChestForm()
    lm_user_bag_unique_form = LMUserBagUniqueForm()
    context = {
        "lm_account":lm_account,
        "lm_user_bag_chest":lm_user_bag_chest,
        "lm_user_bag_chest_form":lm_user_bag_chest_form,
        "lm_user_bag_unique":lm_user_bag_unique,
        "lm_user_bag_unique_form":lm_user_bag_unique_form,
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

def createBagChest(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        LMUserBagChest.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBagChest(request,pk):
    lm_user_bag_chest = get_object_or_404(LMUserBagChest, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_chest.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_chest_form = LMUserBagChestForm(instance=lm_user_bag_chest)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag_chest.name = name
        lm_user_bag_chest.count = count
        lm_user_bag_chest.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_chest_form":lm_user_bag_chest_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_chest_update.html',context)

def deleteBagChest(request,pk):
    lm_user_bag_chest = get_object_or_404(LMUserBagChest, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_chest.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_chest.delete()
    return redirect("read-lm-account", pk=lm_account.id)

def createBagUnique(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        LMUserBagUnique.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBagUnique(request,pk):
    lm_user_bag_unique = get_object_or_404(LMUserBagUnique, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_unique.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_unique_form = LMUserBagUniqueForm(instance=lm_user_bag_unique)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag_unique.name = name
        lm_user_bag_unique.count = count
        lm_user_bag_unique.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_unique_form":lm_user_bag_unique_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_unique_update.html',context)

def deleteBagUnique(request,pk):
    lm_user_bag_unique = get_object_or_404(LMUserBagUnique, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_unique.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_unique.delete()
    return redirect("read-lm-account", pk=lm_account.id)