from django.shortcuts import render, redirect, get_object_or_404
from lm_accounts.models import *
from lm_accounts.forms import *
from lm_accounts.utils import checkModel,checkForm

def createBag(request):
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        account_id = request.POST.get("pk")
        bag_type = request.POST.get("bag_type")
        bag_type = checkModel(bag_type, 'bag')
        lm_account = get_object_or_404(LMUserAccount, id=account_id)
        lm_bag = LMUserBag.objects.get(account_id=lm_account)
        bag_type.objects.create(
            name=name,
            count=count,
            bag_id=lm_bag,
        )
        return redirect("read-lm-account", pk=account_id)

def updateBag(request,type,pk):
    bag_type = checkModel(type, 'bag')
    lm_user_bag = get_object_or_404(bag_type, id=pk)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.bag_id.account_id.id)
    form_type = checkForm(type, 'bag')
    lm_user_bag_form = form_type(instance = lm_user_bag)
    if request.method == "POST":
        name = request.POST.get("name")
        count = request.POST.get("count")
        lm_user_bag.name = name
        lm_user_bag.count = count
        lm_user_bag.save()
        return redirect("read-lm-account", pk=lm_account.id)
    context = {
        "lm_account":lm_account,
        "lm_user_bag_form":lm_user_bag_form,
    }
    return render(request,'lm_accounts/lm_bag/lm_bag_update.html',context)

def deleteBag(request,type,pk):
    bag_type = checkModel(type, 'bag')
    lm_user_bag = get_object_or_404(bag_type, id=pk)
    lm_account = get_object_or_404(LMUserAccount, id=lm_user_bag.bag_id.account_id.id)
    lm_user_bag.delete()
    return redirect("read-lm-account", pk=lm_account.id)