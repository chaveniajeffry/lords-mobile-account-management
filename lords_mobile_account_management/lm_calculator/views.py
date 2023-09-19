from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "home_message":"calculator page",
    }
    return render(request,'lm_calculator/home.html',context)