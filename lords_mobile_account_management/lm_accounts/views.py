from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import LMAccount

@login_required
def home(request):
    context = {
        "home_message":"accounts page",
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
