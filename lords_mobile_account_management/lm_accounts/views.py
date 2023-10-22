from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import LMAccount
from lm_accounts.models import LMUserAccount

@login_required
def home(request):
    lm_accounts = LMUserAccount.objects.all()
    context = {
        "home_message":"accounts page",
        "lm_accounts":lm_accounts,
    }
    return render(request,'lm_accounts/home.html',context)

@login_required
def createAccount(request):
    LMAccount.IGN = ""
    LMAccount.reset_time = ""
    LMAccount.email = ""
    # IGN = models.CharField(max_length=20)
    # reset_time = models.IntegerField()
    # email = models.EmailField(max_length=255)
