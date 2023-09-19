from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "home_message":"accounts page",
    }
    return render(request,'lm_accounts/home.html',context)