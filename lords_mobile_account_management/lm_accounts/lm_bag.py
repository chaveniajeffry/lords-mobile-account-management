from django.shortcuts import render, redirect, get_object_or_404
from lm_accounts.models import *
from lm_accounts.forms import *

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

# LMUserBagSpeedUp
def createBagSpeedUp(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        LMUserBagSpeedUp.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBagSpeedUp(request,pk):
    lm_user_bag_speed_up = get_object_or_404(LMUserBagSpeedUp, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_speed_up.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_speed_up_form = LMUserBagSpeedUpForm(instance=lm_user_bag_speed_up)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag_speed_up.name = name
        lm_user_bag_speed_up.count = count
        lm_user_bag_speed_up.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_speed_up_form":lm_user_bag_speed_up_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_speed_up_update.html',context)

def deleteBagSpeedUp(request,pk):
    lm_user_bag_speed_up = get_object_or_404(LMUserBagSpeedUp, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_speed_up.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_speed_up.delete()
    return redirect("read-lm-account", pk=lm_account.id)

# LMUserBagCombat
def createBagCombat(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        LMUserBagCombat.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBagCombat(request,pk):
    lm_user_bag_combat = get_object_or_404(LMUserBagCombat, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_combat.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_combat_form = LMUserBagCombatForm(instance=lm_user_bag_combat)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag_combat.name = name
        lm_user_bag_combat.count = count
        lm_user_bag_combat.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_combat_form":lm_user_bag_combat_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_combat_update.html',context)

def deleteBagCombat(request,pk):
    lm_user_bag_combat = get_object_or_404(LMUserBagCombat, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_combat.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_combat.delete()
    return redirect("read-lm-account", pk=lm_account.id)

# LMUserBagResources
def createBagResources(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        LMUserBagResources.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBagResources(request,pk):
    lm_user_bag_resources = get_object_or_404(LMUserBagResources, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_resources.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_resources_form = LMUserBagResourcesForm(instance=lm_user_bag_resources)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag_resources.name = name
        lm_user_bag_resources.count = count
        lm_user_bag_resources.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_resources_form":lm_user_bag_resources_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_resources_update.html',context)

def deleteBagResources(request,pk):
    lm_user_bag_resources = get_object_or_404(LMUserBagResources, id=pk)
    lm_user_bag = get_object_or_404(LMUserBag, id=lm_user_bag_resources.bag_id.id)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.account_id.id)
    lm_user_bag_resources.delete()
    return redirect("read-lm-account", pk=lm_account.id)