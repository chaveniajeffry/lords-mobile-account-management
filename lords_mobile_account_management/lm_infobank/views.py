from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "home_message":"infobank page",
    }
    return render(request,'lm_infobank/home.html',context)